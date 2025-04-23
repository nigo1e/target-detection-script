import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "06e427bf-40d0-4d5a-88ce-aec788b0e081"

class Matchmaker:
    def __init__(self, matchmaker_template=None):
        # 创建提示词模板
        self.client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            api_key=os.environ.get("OPENAI_API_KEY"), 
        )
        self.messages = [
            {"role": "system", "content": matchmaker_template},
            {"role": "system", "content": "男生情况: {MALE_INFO}\n女生情况: {FEMALE_INFO}"}
        ]

    def generate_matchmaking_copy(self, context):

        completion = self.client.chat.completions.create(
            model="ep-20250423125256-sj472",
            messages=self.messages,
        )
        print(completion.choices[0].message.content)

if __name__ == "__main__":
    with open("test.txt", "r", encoding="utf-8") as f:
        template = f.read()
    matchmaker = Matchmaker(template)
    context = {
        "MALE_INFO": "小美，20岁，山东青岛，本科在读，平时喜欢打游戏，唱歌，跳舞，身高160，体重100,",
        "FEMALE_INFO": "小帅，24岁，山东济南，大专，厨师，7k，平时喜欢打游戏，篮球，身高176，体重130",
    }
    matchmaker.generate_matchmaking_copy(context)
