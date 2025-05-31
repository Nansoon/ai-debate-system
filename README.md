
# AI Debate System (ChatGPT vs Deepseek)

## 📌 功能简介

- 支持 ChatGPT 与 Deepseek 就任意议题自动化辩论
- 多议题管理：可保存多个辩论主题及进度
- 支持中断与恢复辩论
- 自动生成辩论记录 Word 文档
- 引入第三方点评 AI，总结并给出每轮观点分析与评分

## 📂 文件结构

```
ai_debate_system/
│
├── data/                # 辩论历史存储（JSON）
├── output/              # 输出文档（Word）
├── modules/             # 功能模块（评分、点评等）
├── debate.py            # 主程序
└── README.md            # 使用说明
```

## ▶️ 运行方法

1. 安装依赖：

```bash
pip install openai requests python-docx
```

2. 填写你的 API Key（在 `debate.py` 顶部）

3. 运行程序：

```bash
python debate.py
```

系统将提示你选择已有议题或输入新议题。

---

## 📌 模块说明

- `debate.py`：主流程控制脚本
- `modules/critic.py`：第三方点评 AI 模块
- `modules/utils.py`：通用功能，如保存/加载状态
