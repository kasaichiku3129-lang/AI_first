import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel

load_dotenv()

# 1. モデルの初期化
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 2. 個別のチェーンを定義
joke_chain = ChatPromptTemplate.from_template("{topic}について面白い2行のジョークを教えてください") | model
poem_chain = ChatPromptTemplate.from_template("{topic}について2行の短い詩を作ってください") | model
proverb_chain = ChatPromptTemplate.from_template("{topic}に関する深い格言を一つ教えてください") | model

# 3. RunnableParallel で並列処理を設定
# 辞書のキー（joke, poem）がそのまま実行結果のキーになります
combined_chain = RunnableParallel(
    joke=joke_chain,
    poem=poem_chain,
    proverb=proverb_chain
)

# 4. 実行（2つのモデル呼び出しが同時に行われます）
result = combined_chain.invoke({"topic": "ドラえもん"})

print("=== ジョーク ===")
print(result["joke"].content)

print("\n=== 詩 ===")
print(result["poem"].content)

print("\n===格言===")
print(result["proverb"].content) 