from openai import OpenAI
from modules.utils import load_config
import re
import html  # 添加html模块用于转义

config = load_config()
client = OpenAI(api_key=config["openai_api_key"], base_url=config["openai_base_url"])

def get_critique_and_score(gpt_reply, deepseek_reply):
    prompt = f"""你是一个辩论裁判，请对比以下两位 AI 的发言，从逻辑性、说服力、论据充分度三方面做出点评，并分别给出 10 分制评分。

ChatGPT 的发言：
{gpt_reply}

Deepseek 的发言：
{deepseek_reply}

请输出点评和两个评分，格式如下：
点评：...
评分：ChatGPT X/10, Deepseek Y/10
"""
    response = client.chat.completions.create(
        model=config["openai_model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    content = response.choices[0].message.content
    
    # 清理HTML标签
    clean_content = re.sub(r'<[^>]+>', '', content)  # 移除所有HTML标签
    clean_content = html.escape(clean_content)  # 转义特殊字符
    
    # 提取评分
    match = re.search(r'ChatGPT[：: ]*(\d+)/10.*?Deepseek[：: ]*(\d+)/10', content, re.DOTALL)
    score = {
        "ChatGPT": int(match.group(1)) if match else 7, 
        "Deepseek": int(match.group(2)) if match else 7
    }
    
    return clean_content, score  # 返回清理后的内容