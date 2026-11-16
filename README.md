# Office · Aide Office 文档

Aide `office` 1.2.0，独立分发，MIT 许可。已安装旧版时使用升级入口，保留现有设置与文件。

注册 `office_create`、`office_comments`、`office_comment_edit`、`office_document_search`、`office_document_read`、`office_document_edit` 六项工具。支持通过宿主生成 DOCX/XLSX/PPTX、读取或按锚点修改 DOCX 批注，以及原文/RAG 片段检索；相关文件创建、编辑与来源权限沿用 Aide 现有审批通道。RAG 使用本地检索，不承诺 OCR 或整份文档已读。

必须配合 Aide 原生 Office 工作区执行器及宿主 Python Office 环境（python-docx、openpyxl、python-pptx 等）；Node 入口负责协议注册，不能单独执行 Office 操作。安装 ZIP 不包含宿主执行器或 Python 依赖。需要 Aide 0.1.19.0 RC2 或更新版本，且宿主必须具备 `office-collabora-v1` 能力。缺少该能力的旧同版本宿主会被市场拒绝，请先更新到包含本次集成的 Aide main 源码构建或后续正式版本。Linux 为本次验证环境，Windows/macOS 和实际 SSH 未实测。

从 [v1.2.0 Release](https://github.com/skyelan1999/aide-pkg-office/releases/tag/v1.2.0) 下载 ZIP 与 SHA256SUMS，校验后导入 Aide；也可通过[插件市场](https://skyelan1999.github.io/aide-pkg-shop/)安装。相同 ID/版本无需重复安装。

```sh
sha256sum -c SHA256SUMS
```

本版通过 Release 附件提供安装包及摘要。历史 `packages/v1.1.0/` 仍保留原安装包，旧 Release 的固定提交链接不变；不要把旧包当作本版更新。

本版验证见 [Collabora 集成验收](docs/reviews/2026-11-16-collabora-integration.md)；旧版本记录保留在 docs/reviews/2026-11-14-common-workflow.md 和 docs/release-verification.json。SHA-256 是完整性校验而非签名，Node 插件机制不是权限沙箱。

## 生成正文并核对

在对话中说明文件名、格式和正文；工具参数必须使用对应结构：

```json
{"path":"report.docx","format":"docx","content":{"title":"验收报告","blocks":[{"type":"paragraph","text":"这里是实际正文。"}]}}
```

XLSX 用 `content.sheets=[{name,rows:[[...]]}]`，PPTX 用 `content.slides=[{title,body}]`。DOCX 段落键是 `blocks` 中的 `text`，不是 `paragraphs`；表格使用 `type=table` 和 `rows`。不要把文件生成回执当作正文检查：从自动系统文档打开，或调用 `read_file(source=system-docs,path=相对路径)` 核对；未绑定文档目录时按工具返回的工作区位置打开。

1.1.1 在工具定义中列出上述字段。拒绝未知字段、防止静默丢正文的生成器修复属于 Aide [#892](https://github.com/skyelan1999/aide/issues/892)，需要包含该修复的宿主源码构建；只更新插件不会更新旧宿主的 Python 生成器。此修复不覆盖已有文档，不新增外部调用。

新版本包由 `python3 scripts/package.py <输出目录>` 构建；先运行 `node test.js`。旧 `packages/v1.1.0` 与其摘要保留。


## Collabora Online（1.2.0）

需要同步更新 Aide 宿主；只更新 ZIP 不会给旧宿主增加 WOPI 和 AI 结构化读写接口。市场通过 `office-collabora-v1` 能力条件检查宿主，仅有相同版本号不足以安装。

在 Office 插件设置里配置 `collaboraEnabled=true`、浏览器可访问的 `collaboraUrl`、可选内部 `collaboraInternalUrl`、Collabora 服务可以访问的 `collaboraCallbackUrl`。地址变更后刷新 Aide。默认预览不阻止 AI；切换编辑后按活动状态保护草稿，30 秒无操作且确认保存后允许 AI 写入。预览、编辑、保存、选区/文档交给 AI 都在现有文件查看页面中。

AI 先用 `office_document_read(path,source?,offset?)` 取得地址化文本、分页和 hash，再用 `office_document_edit(path,source?,hash,changes)` 提交精确修改。每项 changes 为 `{id,expectedText,newText}`；段落替换沿用首个文字运行格式，复杂字段和对象拒绝修改，未改动媒体包成员保留原始字节。直接结构化 AI 读写目前支持 DOCX/XLSX/PPTX；其他格式先用编辑器另存为 OOXML。仅读取已保存内容，不代表当前人工草稿已提交。

插件代码仍为 MIT；Collabora 是单独部署的第三方服务，主要 MPL 2.0，不能将插件的 MIT 标成 Collabora 的许可证。CODE 可用于集成验证；企业维护版、商业支持、商标及对应镜像分发条款分别核对。ZIP 不携带 Collabora 二进制、企业订阅或 SLA。

[Collabora 集成验收记录](docs/reviews/2026-11-16-collabora-integration.md)。
