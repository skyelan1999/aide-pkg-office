# Office · Aide Office 文档

Aide `office` 1.1.1 独立分发，MIT 许可。已安装旧版时使用升级入口，保留现有设置与文件。

注册 `office_create`、`office_comments`、`office_comment_edit`、`office_document_search` 四项工具。支持通过宿主生成 DOCX/XLSX/PPTX、读取或按锚点修改 DOCX 批注，以及原文/RAG 片段检索；相关文件创建、编辑与来源权限沿用 Aide 现有审批通道。RAG 使用本地检索，不承诺 OCR 或整份文档已读。

必须配合 Aide 原生 Office 工作区执行器及宿主 Python Office 环境（python-docx、openpyxl、python-pptx 等）；Node 入口负责协议注册，不能单独执行 Office 操作。安装 ZIP 不包含宿主执行器或 Python 依赖。市场兼容基线为 0.1.17.0 RC2。Linux 为本次验证环境，Windows/macOS 和实际 SSH 未实测。

从 [v1.1.1 Release](https://github.com/skyelan1999/aide-pkg-office/releases/tag/v1.1.1) 下载 ZIP 与 SHA256SUMS，校验后导入 Aide；也可通过[插件市场](https://skyelan1999.github.io/aide-pkg-shop/)安装。相同 ID/版本无需重复安装。

```sh
sha256sum -c SHA256SUMS
```

本版通过 Release 附件提供安装包及摘要。历史 `packages/v1.1.0/` 仍保留原安装包，旧 Release 的固定提交链接不变；不要把旧包当作本版更新。

本版验证见 docs/reviews/2026-11-14-common-workflow.md；1.1.0 的历史记录保留在 docs/release-verification.json。SHA-256 是完整性校验而非签名，Node 插件机制不是权限沙箱。

## 生成正文并核对

在对话中说明文件名、格式和正文；工具参数必须使用对应结构：

```json
{"path":"report.docx","format":"docx","content":{"title":"验收报告","blocks":[{"type":"paragraph","text":"这里是实际正文。"}]}}
```

XLSX 用 `content.sheets=[{name,rows:[[...]]}]`，PPTX 用 `content.slides=[{title,body}]`。DOCX 段落键是 `blocks` 中的 `text`，不是 `paragraphs`；表格使用 `type=table` 和 `rows`。不要把文件生成回执当作正文检查：从自动系统文档打开，或调用 `read_file(source=system-docs,path=相对路径)` 核对；未绑定文档目录时按工具返回的工作区位置打开。

1.1.1 在工具定义中列出上述字段。拒绝未知字段、防止静默丢正文的生成器修复属于 Aide [#892](https://github.com/skyelan1999/aide/issues/892)，需要包含该修复的宿主源码构建；只更新插件不会更新旧宿主的 Python 生成器。此修复不覆盖已有文档，不新增外部调用。

新版本包由 `python3 scripts/package.py <输出目录>` 构建；先运行 `node test.js`。旧 `packages/v1.1.0` 与其摘要保留。
