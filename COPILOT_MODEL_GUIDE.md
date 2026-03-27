# GitHub Copilot Pro — Claude Opus 模型使用指南

本文档说明如何在 GitHub Copilot Pro 中选择和使用 **Claude Opus 4.5 / 4.6** 模型（含快速模式）。

---

## 支持的模型概览

GitHub Copilot Pro 支持多个主流 AI 模型，包括：

| 提供商 | 模型 |
|--------|------|
| Anthropic | Claude Haiku 4.5、Claude Sonnet 4 / 4.5 / 4.6、**Claude Opus 4.5 / 4.6** |
| OpenAI | GPT-4o、GPT-4.1、GPT-5 系列、o3-mini 等 |
| Google | Gemini 2.5 Pro、Gemini 3 系列 |
| xAI | Grok Code Fast 1 |

---

## 如何切换到 Claude Opus 模型

### 1. GitHub.com 网页版

1. 打开 [github.com](https://github.com) 并登录。
2. 点击右上角的 **Copilot Chat** 图标（或按 `Ctrl+Shift+I` / `Cmd+Shift+I`）。
3. 在聊天输入框上方找到 **模型选择器**（显示当前所用模型名称的下拉按钮）。
4. 单击该按钮，从列表中选择 **Claude Opus 4.5** 或 **Claude Opus 4.6**。
5. （可选）若列表中出现 **Fast Mode** 开关，将其打开即可启用快速模式。

### 2. VS Code

1. 确保已安装 [GitHub Copilot 扩展](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)。
2. 打开 **Copilot Chat** 侧边栏（快捷键：`Ctrl+Shift+I` / `Cmd+Shift+I`）。
3. 在聊天输入框上方点击 **模型名称按钮**。
4. 在弹出的下拉列表中选择 **Claude Opus 4.5** 或 **Claude Opus 4.6**。
5. 如需快速模式，选择带有 **"Fast"** 标签的对应模型选项。

### 3. JetBrains IDE（IntelliJ、PyCharm 等）

1. 打开 **GitHub Copilot Chat** 工具窗口。
2. 点击聊天面板顶部的 **当前模型名称**。
3. 从下拉列表中选择 **Claude Opus 4.5** 或 **Claude Opus 4.6**。

---

## 快速模式（Fast Mode）

- 快速模式在 **模型选择器** 或模型名称旁以 **"Fast"** / **"Fast Mode"** 标签或切换开关呈现。
- 启用后响应速度更快，适合需要即时反馈的场景；对于需要深度推理的复杂任务，建议使用标准模式。

---

## 注意事项

- 访问 Claude Opus 模型需要有效的 **GitHub Copilot Pro** 订阅。
- Claude Opus 属于高级模型，每次请求会消耗更多的 **premium request** 配额。
- 具体界面入口和可用模型列表可能随 GitHub 版本更新而变化，最新信息请参阅 [GitHub 官方文档](https://docs.github.com/en/copilot/reference/ai-models/supported-models)。
