# %%
# pdf
#  ms docs , hwp, 메모장 , 서식(텍스트, 표, 글씨)
# mistral ai LLM -->  langchain (openAI, mistralAI) APIKey 사용해야 각각의 LLM에 접근할 수 있음
# pip install langchain_core
# pip install langchain_mistralai
# %%
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
import os
# api_key = os.environ.get('MISTRAL_API_KEY')
api_key = "Q4DPG78zp0O2ytxRQfUQjOW6Akg2Gdck"

# import getpass
# import os

# os.environ["MISTRAL_API_KEY"] = getpass.getpass()

# %%

chat = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.5,
    max_retries=2,
    api_key =api_key
)

message = [
    ("system",  "You are a helpful assistant that translates English to Korean. Translate the user sentence."), ("human", "What a nice weather !! ")
]

ai_msg = chat.invoke(message)
print(ai_msg.content)

# %%
# !pip install langchain
# !pip install langchain-community
# !pip install pypdf
from langchain.document_loaders import PyPDFLoader
# %%

file_path = './[이슈리포트 2022-2호] 혁신성장 정책금융 동향.pdf'
loader = PyPDFLoader(file_path)
# %%
contents = loader.load_and_split()
print("*"*10, contents)
# %%
print(contents[2].page_content)
# %%
# !pip install rapidocr_onnxruntime
#  문서에 있는 이미지 추출
loader_img = PyPDFLoader(file_path , extract_images=True)
contents_img = loader_img.load_and_split()

# %%
#! pip install pypdfium2

from langchain.document_loaders import PyPDFium2Loader

loader_total = PyPDFium2Loader(file_path)
contents_total = loader_total.load()
print(contents_total[3].page_content)
# %%

pandas.DataFrame  + matplotlib.pyplot
숫자데이터 
.csv 
.xlsx

DeepL

LLM  -> 데이터생성 (책, 소설, 블로그 ...)
인터넷 정보를 학습
book. ->  LLM  ->  요약
#%%
langchain 내 함수 이용해서, 
    word파일 불러오기
    ppt
    website


LLM, prompt, python, python+API(library), 