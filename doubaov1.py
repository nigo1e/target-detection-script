from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import re
import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "06e427bf-40d0-4d5a-88ce-aec788b0e081"

class Matchmaker:
    def __init__(self, matchmaker_template=None, temperature=0.5):
        # 创建提示词模板
        self.client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            # 从环境变量中获取您的 API Key
            api_key=os.environ.get("ARK_API_KEY"),  # 环境变量名应该是ARK_API_KEY
        )
        self.prompt_template = ChatPromptTemplate([
            ("system", matchmaker_template),
        ])
    
    def generate_matchmaking_copy(self, context):
        full_prompt = self.prompt_template.format(
            MALE_NAME=context["MALE_NAME"],
            FEMALE_NAME=context["FEMALE_NAME"],
            MALE_HEIGHT_DIFFERENCE=context["MALE_HEIGHT_DIFFERENCE"],
            FEMALE_HEIGHT_DIFFERENCE=context["FEMALE_HEIGHT_DIFFERENCE"],
            MALE_GEO_ADVANTAGE=context["MALE_GEO_ADVANTAGE"],
            FEMALE_GEO_ADVANTAGE=context["FEMALE_GEO_ADVANTAGE"],
            MALE_HOMETOWN_CONNECTION=context["MALE_HOMETOWN_CONNECTION"],
            FEMALE_HOMETOWN_CONNECTION=context["FEMALE_HOMETOWN_CONNECTION"],
            MALE_COMMON_INTERESTS=context["MALE_COMMON_INTERESTS"],
            FEMALE_COMMON_INTERESTS=context["FEMALE_COMMON_INTERESTS"],
            PROFESSIONAL_HIGHLIGHTS=context["PROFESSIONAL_HIGHLIGHTS"],
            PERSONALITY_TRAITS=context["PERSONALITY_TRAITS"],
            MARRIAGE_PLAN=context["MARRIAGE_PLAN"],
            FEMALE_CODE=context["FEMALE_CODE"],
            MALE_CODE=context["MALE_CODE"],
        )
        completion = self.client.chat.completions.create(
            # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
            model="ep-20250423125256-sj472",
            messages=[
                {"role": "system", "content": full_prompt},  # 使用完整的提示词
            ],
        )
        print(completion.choices[0].message.content)

# 使用示例
if __name__ == "__main__":
    with open("Copywriter.txt", "r", encoding="utf-8") as f:
        template = f.read()
    matchmaker = Matchmaker(template)
    context = {
        "MALE_NAME": "小帅",
        "FEMALE_NAME": "小美",

        "MALE_HEIGHT_DIFFERENCE": "176cm（比女生高16cm）",
        "FEMALE_HEIGHT_DIFFERENCE": "160cm（比男生矮16cm）",

        "MALE_GEO_ADVANTAGE": "山东济南",
        "FEMALE_GEO_ADVANTAGE": "山东青岛",

        "MALE_HOMETOWN_CONNECTION": "来自山东济南",
        "FEMALE_HOMETOWN_CONNECTION": "来自山东青岛",

        "MALE_COMMON_INTERESTS": "打游戏、篮球",
        "FEMALE_COMMON_INTERESTS": "打游戏、唱歌、跳舞",

        "PROFESSIONAL_HIGHLIGHTS": "厨师，月薪7000元",
        "PERSONALITY_TRAITS": "性格外向、热情、活泼",
        "MARRIAGE_PLAN": "无",

        "FEMALE_CODE": "001",
        "MALE_CODE": "002",
    }
    matchmaker.generate_matchmaking_copy(context)
