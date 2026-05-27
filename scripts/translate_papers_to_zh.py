from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import time
from pathlib import Path

from deep_translator import GoogleTranslator
from PIL import Image
import pdfplumber
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


ROOT = Path(r"C:\Users\31017\Desktop\MLLM for power system surey")
TMP = ROOT / "tmp" / "pdfs"
OUT = ROOT / "output" / "pdf"
FONT_REGULAR = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")
FONT_BOLD = Path(r"C:\Windows\Fonts\NotoSansSC-VF.ttf")

PAPERS = {
    "energy_llm": {
        "source": ROOT
        / "related_papers"
        / "01_power_energy_surveys"
        / "1-s2.0-S0306261925018069-main.pdf",
        "title_en": "Large Language Models Meet Energy Systems: Opportunities, Challenges, and Future Perspectives",
        "title_zh": "大语言模型遇见能源系统：机遇、挑战与未来展望",
        "out_name": "大语言模型遇见能源系统_机遇挑战与未来展望_中文译文.pdf",
        "mode": "text",
    },
    "power_ai_large_models": {
        "source": ROOT
        / "related_papers"
        / "01_power_energy_surveys"
        / "AIk.pdf",
        "title_en": "AI Large Models for Power System: A Survey and Outlook",
        "title_zh": "电力系统中的人工智能大模型：综述与展望",
        "out_name": "电力系统中的人工智能大模型_综述与展望_中文译文.pdf",
        "mode": "ocr",
    },
}


GLOSSARY = {
    "大型语言模型满足能源系统": "大语言模型遇见能源系统",
    "大型语言模型": "大语言模型",
    "电力系统大型模型": "电力系统大模型",
    "人工智能大型模型": "人工智能大模型",
    "智能电力系统": "智能电力系统",
    "提示工程": "提示工程",
    "知识增强": "知识增强",
    "微调": "微调",
    "多模态集成": "多模态融合",
    "自治代理": "自主智能体",
    "代理": "智能体",
    "负荷预测": "负荷预测",
}


def log(msg: str) -> None:
    print(msg, flush=True)


def ensure_dirs() -> None:
    TMP.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def cache_path(name: str) -> Path:
    return TMP / f"{name}_translation_cache.json"


def load_cache(name: str) -> dict[str, str]:
    p = cache_path(name)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {}


def save_cache(name: str, cache: dict[str, str]) -> None:
    cache_path(name).write_text(
        json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def clean_pdf_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\uf0b7", "•")
    text = re.sub(r"([A-Za-z])- *\n *([a-z])", r"\1\2", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_text_pdf(pdf_path: Path, cache_name: str) -> str:
    text_path = TMP / f"{cache_name}_extracted_en.txt"
    if text_path.exists():
        return text_path.read_text(encoding="utf-8")

    pages: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = clean_pdf_text(page.extract_text() or "")
            pages.append(f"\n\n[Page {i}]\n{text}")
            log(f"extracted text page {i}/{len(pdf.pages)}")
    text = "\n".join(pages)
    text_path.write_text(text, encoding="utf-8")
    return text


def render_pdf_pages(pdf_path: Path, cache_name: str) -> list[Path]:
    img_dir = TMP / f"{cache_name}_pages"
    img_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted(img_dir.glob("page-*.png"))
    if existing:
        return existing

    import subprocess

    prefix = img_dir / "page"
    subprocess.run(
        [
            "pdftoppm",
            "-png",
            "-r",
            "150",
            str(pdf_path),
            str(prefix),
        ],
        check=True,
    )
    return sorted(img_dir.glob("page-*.png"))


def ocr_image(reader, image_path: Path, page_index: int) -> str:
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    parts: list[tuple[str, Image.Image]] = []

    if page_index == 1:
        # First article page has a full-width title/abstract followed by columns.
        top_h = int(h * 0.61)
        parts.append(("top", img.crop((0, 0, w, top_h))))
        parts.append(("left", img.crop((0, top_h, int(w * 0.52), int(h * 0.94)))))
        parts.append(("right", img.crop((int(w * 0.48), top_h, w, int(h * 0.94)))))
    else:
        top = int(h * 0.07)
        bottom = int(h * 0.94)
        parts.append(("left", img.crop((0, top, int(w * 0.52), bottom))))
        parts.append(("right", img.crop((int(w * 0.48), top, w, bottom))))

    page_text: list[str] = []
    for label, crop in parts:
        tmp_img = image_path.with_name(f"{image_path.stem}_{label}.png")
        crop.save(tmp_img)
        result = reader.readtext(str(tmp_img), detail=0, paragraph=True)
        text = "\n".join(str(x) for x in result)
        page_text.append(text)
    return clean_pdf_text("\n\n".join(page_text))


def extract_ocr_pdf(pdf_path: Path, cache_name: str) -> str:
    text_path = TMP / f"{cache_name}_ocr_en.txt"
    if text_path.exists():
        return text_path.read_text(encoding="utf-8")

    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    import easyocr

    images = render_pdf_pages(pdf_path, cache_name)
    reader = easyocr.Reader(["en"], gpu=False, verbose=False)
    pages: list[str] = []
    for idx, img in enumerate(images, start=1):
        log(f"OCR page {idx}/{len(images)}")
        text = ocr_image(reader, img, idx)
        pages.append(f"\n\n[Page {idx}]\n{text}")
        text_path.write_text("\n".join(pages), encoding="utf-8")
    return "\n".join(pages)


def split_chunks(text: str, max_chars: int = 3600) -> list[str]:
    blocks = re.split(r"(\n\s*\n)", text)
    chunks: list[str] = []
    current = ""
    for block in blocks:
        if len(current) + len(block) <= max_chars:
            current += block
        else:
            if current.strip():
                chunks.append(current.strip())
            if len(block) > max_chars:
                for i in range(0, len(block), max_chars):
                    chunks.append(block[i : i + max_chars].strip())
                current = ""
            else:
                current = block
    if current.strip():
        chunks.append(current.strip())
    return [c for c in chunks if c.strip()]


def apply_glossary(text: str) -> str:
    for src, dst in GLOSSARY.items():
        text = text.replace(src, dst)
    return text


def translate_text(text: str, cache_name: str) -> str:
    cache = load_cache(cache_name)
    translator = GoogleTranslator(source="en", target="zh-CN")
    chunks = split_chunks(text)
    translated: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        key = sha1(chunk)
        if key in cache:
            zh = cache[key]
        else:
            log(f"translating chunk {i}/{len(chunks)}")
            for attempt in range(1, 6):
                try:
                    zh = translator.translate(chunk)
                    break
                except Exception as exc:
                    if attempt == 5:
                        raise
                    log(f"translation retry {attempt}: {exc}")
                    time.sleep(2 * attempt)
            zh = apply_glossary(zh)
            cache[key] = zh
            save_cache(cache_name, cache)
            time.sleep(0.3)
        translated.append(zh)
    return "\n\n".join(translated)


def setup_fonts() -> tuple[str, str]:
    regular = "NotoSansSC"
    bold = "NotoSansSC-Bold"
    pdfmetrics.registerFont(TTFont(regular, str(FONT_REGULAR)))
    pdfmetrics.registerFont(TTFont(bold, str(FONT_BOLD)))
    return regular, bold


def make_pdf(title_zh: str, title_en: str, body: str, out_path: Path) -> None:
    regular, bold = setup_fonts()
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ChineseTitle",
        parent=styles["Title"],
        fontName=bold,
        fontSize=20,
        leading=28,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#111111"),
        wordWrap="CJK",
        spaceAfter=8,
    )
    subtitle_style = ParagraphStyle(
        "EnglishSubtitle",
        parent=styles["Normal"],
        fontName=regular,
        fontSize=9,
        leading=13,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555"),
        wordWrap="CJK",
        spaceAfter=10,
    )
    note_style = ParagraphStyle(
        "Note",
        parent=styles["Normal"],
        fontName=regular,
        fontSize=9,
        leading=14,
        textColor=colors.HexColor("#666666"),
        wordWrap="CJK",
        spaceAfter=12,
    )
    body_style = ParagraphStyle(
        "ChineseBody",
        parent=styles["BodyText"],
        fontName=regular,
        fontSize=10.5,
        leading=17,
        alignment=TA_JUSTIFY,
        firstLineIndent=18,
        wordWrap="CJK",
        spaceAfter=7,
    )
    page_style = ParagraphStyle(
        "PageLabel",
        parent=styles["Heading3"],
        fontName=bold,
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#2f5f8f"),
        wordWrap="CJK",
        spaceBefore=10,
        spaceAfter=6,
    )

    doc = SimpleDocTemplate(
        str(out_path),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=title_zh,
        author="Codex translation workflow",
    )

    story = [
        Paragraph(html.escape(title_zh), title_style),
        Paragraph(html.escape(title_en), subtitle_style),
        Paragraph(
            "说明：本文档为基于原文 PDF 生成的中文译文版，采用可读性优先的单栏排版；公式、图表与参考文献编号可能未完全复刻原版版式。",
            note_style,
        ),
        Spacer(1, 5 * mm),
    ]

    body = body.replace("\r\n", "\n").replace("\r", "\n")
    parts = re.split(r"(\[第?\s*Page\s*\d+\]|\[Page\s*\d+\])", body)
    paragraphs: list[str] = []
    for part in parts:
        if not part.strip():
            continue
        label_match = re.fullmatch(r"\[第?\s*Page\s*(\d+)\]|\[Page\s*(\d+)\]", part.strip())
        if label_match:
            page_no = label_match.group(1) or label_match.group(2)
            paragraphs.append(f"@@PAGE@@原文第 {page_no} 页")
            continue
        for para in re.split(r"\n\s*\n|\n", part):
            para = para.strip()
            if para:
                paragraphs.append(para)

    for para in paragraphs:
        if para.startswith("@@PAGE@@"):
            story.append(Paragraph(html.escape(para.replace("@@PAGE@@", "")), page_style))
            continue
        safe = html.escape(para)
        story.append(Paragraph(safe, body_style))

    def footer(canvas, doc_obj):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#777777"))
        canvas.drawCentredString(A4[0] / 2, 10 * mm, f"{doc_obj.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def process(name: str) -> Path:
    spec = PAPERS[name]
    source = spec["source"]
    log(f"processing {source.name}")
    if spec["mode"] == "text":
        en = extract_text_pdf(source, name)
    else:
        en = extract_ocr_pdf(source, name)
    (TMP / f"{name}_source_en.txt").write_text(en, encoding="utf-8")
    zh = translate_text(en, name)
    zh = zh.replace("大语言模型遇见能源系统：机遇、挑战、和未来视角", PAPERS[name]["title_zh"])
    zh = zh.replace("电力系统的 AI 大型模型：调查和展望", PAPERS[name]["title_zh"])
    (TMP / f"{name}_translated_zh.txt").write_text(zh, encoding="utf-8")
    out_path = OUT / spec["out_name"]
    make_pdf(spec["title_zh"], spec["title_en"], zh, out_path)
    log(f"written {out_path}")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--paper",
        choices=["all", *PAPERS.keys()],
        default="all",
    )
    args = parser.parse_args()
    ensure_dirs()
    names = list(PAPERS) if args.paper == "all" else [args.paper]
    for name in names:
        process(name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
