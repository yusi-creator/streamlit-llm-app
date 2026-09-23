import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=150)

expert_messages = {
    "栄養": "栄養の専門家として、100文字以内で答えてください。",
    "節約": "節約の専門家として、100文字以内で答えてください。"
}

def get_answer(input_text, expert):
    response = llm.invoke([
        SystemMessage(content=expert_messages[expert]),
        HumanMessage(content=input_text)
    ])
    return response.content

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("食事アドバイス")
st.write("食べ物を入力すると、選択した専門家が100文字以内でアドバイスします。")
st.write("専門家を選択し、食べ物を入力して「実行」を押してください。")

expert = st.radio("専門家を選択", ["栄養", "節約"])
input_text = st.text_input("食べ物を入力")

if st.button("実行"):
    try:
        with st.spinner("回答を生成中..."):
            answer = get_answer(input_text, expert)
        st.session_state.messages.append((input_text, answer))
        st.write(answer)
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

if st.session_state.messages:
    st.subheader("会話履歴")
    for question, answer in st.session_state.messages:
        st.write(f"入力：{question}")
        st.write(f"回答：{answer}")