from langchain_openai import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

llm = ChatOpenAI()  # ChatGPT APIを呼んでくれる機能
message = "頑張っている私に一言！"  # あなたの質問をここに書く

messages = [
    SystemMessage(content="絶対に関西弁で返答してください"),
    HumanMessage(content=message)
]
response = llm.invoke(messages)
print(response.content)

# content='Hello! How can I assist you today?' additional_kwargs={} example=False