import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import (SystemMessage, HumanMessage, AIMessage)

def select_model():
    """サイドバーの入力を読み取って、設定済みのLLMインスタンスを返す関数"""
    st.sidebar.title("Options")
    
    # モデルの選択
    model_choice = st.sidebar.radio("Choose a model:", ("GPT-4o-mini", "GPT-4"))
    if model_choice == "GPT-4o-mini":
        model_name = "gpt-4o-mini"
    else:
        model_name = "gpt-4"

    # 気温（Temperature）の設定
    temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=2.0, value=0.0, step=0.1)

    # コスト表示（ダミー）
    st.sidebar.markdown("## Costs")
    st.sidebar.markdown("**Total cost**")
    st.sidebar.markdown("- $0.02") # 先ほど確認した実際の利用額っぽく

    # 設定を反映したChatOpenAIを返す
    return ChatOpenAI(temperature=temperature, model_name=model_name)

def main():
    st.set_page_config(
        page_title="My Great ChatGPT",
        page_icon="🤗"
    )
    
    # 1. サイドバーで設定したモデルを取得（ここが重要！）なんです

    llm = select_model()

    st.header("My Great ChatGPT 🤗")

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]

    # サイドバーの「Clear」ボタンが押されたら履歴をリセット
    if st.sidebar.button("Clear Conversation"):
        st.session_state.messages = [SystemMessage(content="You are a helpful assistant.")]
        # 再読み込みして画面をスッキリさせる
        st.rerun()

    # ユーザーの入力を監視
    if user_input := st.chat_input("聞きたいことを入力してね！"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        with st.spinner("ChatGPT is typing ..."):
            # 反映された llm を使って回答生成
            response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴の表示
    for message in st.session_state.messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)

if __name__ == '__main__':
    main()