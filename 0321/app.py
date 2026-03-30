from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# 1. テンプレートの定義（2箇所の変数を用意）
prompt = ChatPromptTemplate.from_messages([
    ("system", "あなたは{expertise}の専門家です。簡潔に説明してください。"),
    ("user", "{topic}について初心者向けに2つポイントを一言説明してください。")
])

# 2. 埋め込み用データ（キーと変数名を一致させる）
parameters = {
    "expertise": "プログラミング教育",  # {expertise} に入る値
    "topic": "Pythonクラスの基本概念"     # {topic} に入る値
}

# 3. LLMの設定
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

# 4. チェーンを作成して実行
chain = prompt | llm

# invokeに辞書（parameters）を渡す
response = chain.invoke(parameters)

print("--- LLMからの応答 ---")
print(response.content)