import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "06e427bf-40d0-4d5a-88ce-aec788b0e081"
class Matchmaker:
    def __init__(self, matchmaker_template=None,example_answer=None):
        self.client = OpenAI(
            base_url="https://ark.cn-beijing.volces.com/api/v3",
            api_key=os.environ.get("OPENAI_API_KEY"), 
        )
        self.messages = [
            {"role": "system", "content": matchmaker_template},
            {"role": "assistant", "content": example_answer},
            {"role": "system", "content": "男生情况: {MALE_INFO}\n女生情况: {FEMALE_INFO}\nFEMALE_CODE: {MALE_CODE}\nMALE_CODE: {FEMALE_CODE}"}
        ]
    def generate_matchmaking_copy(self, context):
        self.messages[-1]["content"] = self.messages[-1]["content"].format(**context)
        completion = self.client.chat.completions.create(
            model="ep-20250423125256-sj472",
            messages=self.messages,
        )
        print(completion.choices[0].message.content)
if __name__ == "__main__":
    with open("template.txt", "r", encoding="utf-8") as f:
        template = f.read()
    with open("example_output.txt", "r", encoding="utf-8") as f:
        example_output = f.read()
    context = {
        "MALE_INFO": "小美，20岁，山东青岛，本科在读，打篮球，唱歌，跳舞，身高200，体重100,",
        "FEMALE_INFO": "小帅，24岁，山东济南，大专，厨师，7k，篮球，唱歌，跳舞，身高176，体重130",
        "FEMALE_CODE": "102",
        "MALE_CODE": "101",
    }
    matchmaker = Matchmaker(template,example_output)
    matchmaker.generate_matchmaking_copy(context)
