from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

import os

# 環境変数の読み込み
load_dotenv()

def create_profile_rag():
    # テキストファイルの読み込み
    loader = TextLoader("profile.txt",encoding="utf-8")
    documents = loader.load()
    
    # テキストの分割
    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=0
    )
    texts = text_splitter.split_documents(documents)
    
    # ベクトルストアの作成
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    
    # 質問応答チェーンの作成
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=1.0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    
    return qa_chain

def main():
    qa_chain = create_profile_rag()
    
    for i in range(3):
        question = input("質問を入力してください:")
        print(f"\n質問: {question}")
        answer = qa_chain.invoke({"query": question})
        print(f"回答: {answer['result']}")

if __name__ == "__main__":
    main()