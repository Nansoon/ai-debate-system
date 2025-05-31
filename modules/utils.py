
import os
import json
import streamlit as st


def save_state(topic, chat_history, round_no):
    with open(f"data/{topic}.json", "w", encoding="utf-8") as f:
        json.dump({"topic": topic, "chat_history": chat_history, "round_no": round_no}, f, ensure_ascii=False, indent=2)

def load_state(topic):
    file_path = f"data/{topic}.json"
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 验证字段完整性
    if "topic" not in data or "chat_history" not in data or "round_no" not in data:
        raise ValueError(f"文件字段缺失，请删除该议题并重新创建：{file_path}")

    return data["topic"], data["chat_history"], data["round_no"]


    required_keys = ("topic", "chat_history", "round_no")
    if not all(k in data for k in required_keys):
        raise KeyError(f"文件字段缺失，请删除该议题并重新创建：{path}")

    return data["topic"], data["chat_history"], data["round_no"]


def list_saved_debates():
    os.makedirs("data", exist_ok=True)
    valid_debates = []
    for f in os.listdir("data"):
        if f.endswith(".json"):
            try:
                with open(os.path.join("data", f), "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if "topic" in data and "chat_history" in data and "round_no" in data:
                        valid_debates.append(f[:-5])
            except Exception:
                continue  # 忽略无效或损坏文件
    return valid_debates


def load_config():
    # ✅ 优先使用云端的 secrets（部署在 Streamlit Cloud）
    try:
        if "openai_api_key" in st.secrets:
            return {
                "openai_api_key": st.secrets["openai_api_key"],
                "openai_base_url": st.secrets["openai_base_url"],
                "openai_model": st.secrets.get("openai_model", "gpt-4o"),
                "deepseek_api_key": st.secrets["deepseek_api_key"],
                "deepseek_api_url": st.secrets["deepseek_api_url"]
            }
    except Exception:
        pass  # 👈 如果没有 secrets，就自动 fallback 到本地

    # ✅ 本地 fallback：从 config.json 加载
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)


