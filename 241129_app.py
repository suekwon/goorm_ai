import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
import os

# API 키 설정
api_key = os.environ.get('MISTRAL_API_KEY')

# MistralClient 초기화
chat = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.5,
    max_retries=2,
    api_key=api_key,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# 프롬프트 템플릿 설정
chef_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a fine dining Korean food chef. You will be asked to make a dish with easy to find ingredients. Do NOT reply with anything else. Also, always answer in Korean."),
        ("human", "I want to cook {menu}."),
    ]
)

# 체인 설정
chef_chain = chef_prompt | chat

# Streamlit 앱 설정
st.title("Korean Fine Dining Chatbot")

# 세션 상태 초기화
if 'message' not in st.session_state:
    st.session_state.message = []

# 사용자 입력
user_input = st.text_input("You:", value=st.session_state.input, key="input")

# 사용자 입력 처리
if user_input:
    st.session_state.message.append({"role": "user", "content": user_input})

    response = chef_chain.invoke({"menu": user_input})
    st.session_state.message.append(
        {"role": "ai", "content": response.content})
