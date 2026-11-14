# Office 1.1.1 常用流程验收

对应集中问题 skyelan1999/aide#892。工具参数列出 DOCX blocks、XLSX sheets、PPTX slides 的字段和示例。独立仓库的测试不再依赖仓库外的宿主 registry.json。

- `node test.js` 通过；打包器再次执行相同验证，ZIP CRC 与内容白名单检查通过。
- 真实隔离 Aide HTTP/DOM 与原生工具执行器，使用合成项目及无付费确定性提供商：旧 1.1.0 正常升级至 1.1.1；工具 surface 正常加载。
- 复现旧生成器以 content.paragraphs 生成文件但丢正文；修复后的宿主拒绝未知字段，给出 title/blocks 的准确提示；独立文件请求确认没有创建残缺文件。
- 通过正确 blocks 创建含段落及表格的 DOCX；从绑定的 system-docs 独立 read_file，核对正文、表格列名和数值 42。
- 宿主 Go 集成验证同时覆盖 DOCX/XLSX/PPTX 的错误字段不写盘，及既有生成与 XLSX 编辑/版本冲突行为。

严格内容检查属于宿主 Aide 的 Python 生成器，单独更新插件不会修改旧宿主。包内示例是合成输入，验证不代表真实账户、SSH、WPS/Office 桌面或外部硬件验收。Aide 本轮不发布 Release；独立插件 main、Release、市场和运行实例升级分别核对。
