# 《计算机学报》模板版初稿编译说明

生成日期：2026-05-21

## 1. 模板检查结果

- `template/main.tex`：UTF-8 编码，文件头指定 `% !TeX program = xelatex`，主模板入口。
- `template/CjC.cls`：模板文档类，内部基于 `ctexart`，适合 XeLaTeX 中文编译。
- `template/CjC_template_tex.tex`：旧模板示例，包含 GBK/CJK 片段，当前不作为主入口，避免中文乱码。
- `template/` 中未发现 `.bst` 或 `.bib` 文件。
- `template/` 中包含图片/依赖：`CJC1.pdf`、`yourphotofilename.jpg`、`captionhack.sty`、`picins.sty`、`mtpro2.sty`。

## 2. 本轮生成文件

- `output/main.tex`：基于 `template/main.tex` 生成，保留 `CjC` 文档类、原有宏包、首页结构、标题/摘要/关键词/参考文献区域，只替换模板正文占位内容。
- `output/references.bib`：BibTeX 条目仅来自 verified 或 metadata verified 文献；缺失元数据使用 `TODO` 标注，未补造 DOI、页码或期刊名。
- `output/figures/`：图件目录，已放入模板示例图 `CJC1.pdf`；后续正式图件应放入此目录。
- `output/CjC.cls`、`output/captionhack.sty`、`output/picins.sty`、`output/mtpro2.sty`、`output/yourphotofilename.jpg`：从模板复制的本地编译依赖。

## 3. 推荐编译命令

请在 `output/` 目录执行，必须使用 XeLaTeX，不要使用 `pdflatex`。

```powershell
cd "C:\Users\31017\Desktop\MLLM for power system surey\output"
xelatex -interaction=nonstopmode main.tex
bibtex main
xelatex -interaction=nonstopmode main.tex
xelatex -interaction=nonstopmode main.tex
```

## 4. 字体与中文说明

`main.tex` 明确使用 XeLaTeX，并在 `CjC.cls` 的 `ctexart` 基础上设置常见 Windows 字体：

- 英文主字体：Times New Roman
- 中文主字体：SimSun
- 中文黑体：SimHei
- 中文等宽/仿宋：FangSong

若在非 Windows 环境编译，可将这些字体替换为系统存在的中文字体，例如 Noto Serif CJK SC、Noto Sans CJK SC。

## 5. 已知 TODO

- 作者、单位、通信作者、基金、作者简介、收稿日期、联系方式仍需作者补全。
- 图1 当前为正文中的占位说明，正式投稿前应绘制黑白矢量图并放入 `output/figures/`。
- 部分中文文献缺少卷期、页码或 DOI，已在 `references.bib` 中用 `TODO` 标注，后续需通过知网/期刊官网核对。
- 当前使用 `unsrt` BibTeX 样式接入 `references.bib`。若最终严格按《计算机学报》排版，建议在定稿阶段将 `.bbl` 内容人工整理为模板推荐的 `thebibliography` 格式，并为中文参考文献补英文对照。

## 6. 禁止事项

- 不要使用 `pdflatex`。
- 不要从 Markdown 直接转换 PDF。
- 不要用未核验文献补充参考文献。
- 不要补造 DOI、卷期、页码、会议名或期刊名。
