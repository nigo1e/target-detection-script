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
        return completion.choices[-1].message.content
if __name__ == "__main__":
    with open("template.txt", "r", encoding="utf-8") as f:
        template = f.read()
    with open("example_output.txt", "r", encoding="utf-8") as f:
        example_output = f.read()
    # context = {
    #     "FEMALE_INFO": "小白，24岁，山东济南，大专，厨师，7k，篮球，唱歌，跳舞，身高176，体重130",
    #     "MALE_INFO": "小明，20岁，山东青岛，本科在读，打篮球，唱歌，跳舞，身高200，体重100,",
    #     "FEMALE_CODE": "122",
    #     "MALE_CODE": "935",
    # }
    # context = {
    #     "FEMALE_INFO": "小红，26岁，北京，本科，设计师，8k，瑜伽，阅读，旅行，身高165，体重50",
    #     "MALE_INFO": "小刚，28岁，上海，硕士，程序员，12k，游泳，徒步，摄影，身高180，体重70",
    #     "FEMALE_CODE": "722",
    #     "MALE_CODE": "689",
    # }
    # context = {
    #     "FEMALE_INFO": "小红，26岁，北京，本科，设计师，8k，瑜伽，阅读，旅行，身高165，体重50",
    #     "MALE_INFO": "小刚，28岁，上海，硕士，程序员，12k，游泳，徒步，摄影，身高180，体重70",
    #     "FEMALE_CODE": "122",
    #     "MALE_CODE": "999",
    # }
    # context = {
    #     "FEMALE_INFO": "小芳，22岁，广州，大专，服务员，6k，画画，跳舞，烹饪，身高160，体重45",
    #     "MALE_INFO": "小强，30岁，深圳，本科，教师，9k，跑步，阅读，电影，身高175，体重65",
    #     "FEMALE_CODE": "333",
    #     "MALE_CODE": "888",
    # }
    context = {
        "FEMALE_INFO": "小丽，25岁，成都，本科，记者，7.5k，摄影，写作，徒步，身高168，体重55",
        "MALE_INFO": "小杰，27岁，杭州，硕士，工程师，11k，健身，旅行，音乐，身高182，体重75",
        "FEMALE_CODE": "444",
        "MALE_CODE": "777",
    }
    matchmaker = Matchmaker(template,example_output)
#默认创建matchmaking.md文件，如果文件已存在，则追加写入
    if not os.path.exists("matchmaking.md"):
        os.mknod("matchmaking.md")
    with open("matchmaking.md", "a", encoding="utf-8") as f:
        answer = matchmaker.generate_matchmaking_copy(context)
        f.write(answer)
    print("MALE CODE:", context["MALE_CODE"])
    print("FEMALE CODE:", context["FEMALE_CODE"])