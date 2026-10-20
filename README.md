# Office · Aide Office 文档

Aide `office` 1.1.0 独立分发，MIT 许可。安装 ZIP 与已有市场包保持逐字节一致。

注册 `office_create`、`office_comments`、`office_comment_edit`、`office_document_search` 四项工具。支持通过宿主生成 DOCX/XLSX/PPTX、读取或按锚点修改 DOCX 批注，以及原文/RAG 片段检索；相关文件创建、编辑与来源权限沿用 Aide 现有审批通道。RAG 使用本地检索，不承诺 OCR 或整份文档已读。

必须配合 Aide 原生 Office 工作区执行器及宿主 Python Office 环境（python-docx、openpyxl、python-pptx 等）；Node 入口负责协议注册，不能单独执行 Office 操作。安装 ZIP 不包含宿主执行器或 Python 依赖。市场兼容基线为 0.1.17.0 RC2。Linux 为本次验证环境，Windows/macOS 和实际 SSH 未实测。

从 [v1.1.0 Release](https://github.com/skyelan1999/aide-pkg-office/releases/tag/v1.1.0) 的固定提交链接下载 ZIP 与 SHA256SUMS，校验后导入 Aide；也可通过[插件市场](https://skyelan1999.github.io/aide-pkg-shop/)安装。相同 ID/版本无需重复安装。

```sh
sha256sum -c SHA256SUMS
```

安装包位于 packages/v1.1.0/，保留原 LICENSE、入口、manifest、测试与包内说明；外部 README 不重新写入原 ZIP。Release 使用仓库固定提交链接，没有另行上传二进制附件。

验证结果见 docs/release-verification.json。SHA-256 是完整性校验而非签名，Node 插件机制不是权限沙箱。
