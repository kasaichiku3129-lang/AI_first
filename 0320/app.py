from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

chat_model = ChatOpenAI(model="gpt-4o-mini")

prompt_txt = ChatPromptTemplate.from_messages(
    [
        ("system", "あなたは親切なアシスタントです。"),
        ("human", "{country}の首都をおしえてください。"),
    ]
)

output_parser = StrOutputParser()

chain = prompt_txt | chat_model | output_parser

result = chain.invoke("カナダ")

print(result)