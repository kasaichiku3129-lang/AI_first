import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 環境変数の読み込み
load_dotenv()

#1　独自の関数を定義
def letter_count(text:str) -> int:
    return len(text)

#コンポーネントの初期化
llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template(
    "次に関連する英単語を英語で5つ出力してください（カンマ区切り）： {question}"
)

#　チェーンの構築
#  カッコ()で囲むことで、複数行に分けて美しく記述できます

chain = (
    prompt | 
    llm |
    StrOutputParser() |
    letter_count
    )

question = "人工知能"
result = chain.invoke({"question": question})

print(f"トピック: {question}")
print(f"回答（文字列の数）：{result}")
