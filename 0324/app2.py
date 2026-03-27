from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI(model='gpt-4o-mini')

# 1. 前処理用のカスタム関数 (RunnableLambdaへ自動変換)
def preprocess(input_data):
    return input_data.strip().lower()

# 2. データの保持と加工の並列処理 (RunnableParallel)
# original_inputを保持しつつ、加工したデータをモデルへ
chain = (
    {"processed_text": RunnableLambda(preprocess), "raw": RunnablePassthrough()}
    | ChatPromptTemplate.from_template("{processed_text}について詳しく解説して")
    | model
)

# 実行
result = chain.invoke("LangChain")

print(result)