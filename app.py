from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=50)

def get_answer(input_text, expert):
    if expert == "栄養":
        system_message = "栄養の専門家として、100文字以内で答えてください。"
    else:
        system_message = "節約の専門家として、100文字以内で答えてください。"
    response = llm.invoke([
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ])
    return response.content

st.title("食事アドバイス")
st.write("食べ物を入力すると、選択した専門家が100文字以内でアドバイスします。")
st.write("専門家を選択し、食べ物を入力して「実行」を押してください。")
expert = st.radio("専門家を選択", ["栄養", "節約"])
input_text = st.text_input("食べ物を入力")

if st.button("実行"):
    answer = get_answer(input_text, expert)
    st.write(answer)