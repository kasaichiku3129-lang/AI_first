from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# モデルを使ってプロンプトを送信
llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("英単語を3つのみ返却して")
print(response)