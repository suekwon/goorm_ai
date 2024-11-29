# %%
# 응답하는 중에 답변을 보여주기
from langchain.callbacks import StreamingStdOutCallbackHandler

# 답변을 리스트로 항상
from langchain.schema import BaseOutputParser

from langchain.schema import HumanMessage,  AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_mistralai import ChatMistralAI
import os
api_key = os.environ.get('MISTRAL_API_KEY')

chat = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0.5,
    max_retries=2,
    api_key=api_key,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

# %%

message = [
    ("system",  "You are a helpful assistant that translates English to Korean. Translate the user sentence."), ("human", "What a nice weather !! ")
]

ai_msg = chat.invoke(message)
print(ai_msg.content)

# %%

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helpful assistant that translates {input_lang} to {output_lang}. Translate the user sentence."),
        ("human", "{input_sentence }")
    ]
)

chain = prompt | llm

chain.invoke(
    {
        "input_lang": "English",
        "output_lang": "Korean",
        "input_sentence": "What a nice weather !!"
    }
)


# %%

message = [
    SystemMessage(
        "You are a helpful assistant that have expert knowledge about geography. Answer to the user sentence in Korean."
    ),
    AIMessage(
        "Hello, I am a geography expert, My name is Goormi."
    ),
    HumanMessage(
        "How far is the Bali from the South Korea? and also, how many hours does it take to get there?"
    )
]

chat.predict_messages(message).content

# %%

message = [
    SystemMessage(
        "You are a helpful assistant that have expert knowledge about geography. Answer to the user sentence in {country}."
    ),
    AIMessage(
        "Hello, I am a geography expert, My name is {name}."
    ),
    HumanMessage(
        "How far is the {ACountry} from the {BCountry}? and also, how many hours does it take to get there?"
    )
]

template = ChatPromptTemplate.from_template(
    "How far is the {ACountry} from the {BCountry}?"
)
prompt = template.format(
    ACountry="Japan",
    BCountry="USA"
)
chat.predict(prompt)

# %%
template = ChatPromptTemplate.from_messages(
    [
        ("system",
         "You are a helpful assistant that have expert knowledge about geography. Answer to the user sentence in {language}."),
        ("ai", "Hi, my name is {name}"),
        ("human", "How far is the {ACity} from the {BCity}? and also, how many hours does it take to get there?"),]
)

prompt = template.format_messages(
    language="Korean", name="HonamICT", ACity="Seoul", BCity="LA")
# %%
response = chat.predict_messages(prompt)
# %%
response.content.split("\n")[2]
# %%

template = ChatPromptTemplate.from_messages(
    [("system", "You are a list generating machine. Everyhthing you are asked will answered as a comma  seperate list of max  {max_item}. Do NOT reply with anything else."),
     ("human", "{question}"),]
)

prompt = template.format_messages(
    max_item=5,
    question="What are the top 5 countries with the highest GDP?"
)
response = chat.predict_messages(prompt)
# %%
response.content.strip().split(",")[:5]
# %%


class CommaOutputParser(BaseOutputParser):
    def parse(self, output):
        item = output.strip().split(",")
        return list(map(str.strip, item))


p = CommaOutputParser()
p.parse("hello, how, are, you")

# %%


p.parse(response.content)
# %%
chain = template | chat
chain.invoke(
    {
        "max_item": 2,
        "question": "What are the top 2 countries with the highest GDP?"
    }
)

# %%

# chef_bot
chef_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a fine dining Korean food chef. You will be asked to make a dish with easy to find ingredients. Do NOT reply with anything else. Also, always answer in Korean."),
        ("human", "I want to cook {menu}."),
    ]

)
chef_chain = chef_prompt | chat
chef_chain.invoke("떡볶이")
# %%
veg_chef_prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a vegeterian chef specialist. You find alternative ingredients and explain their preperation. You don't  redically mondify the recipe. If there is no alternative  for a food just say you don't know how to replace it. Also, always answer in Korean."),
     ("human", "I want to know  the  vegeterian {receipe}.")])
veg_chain = veg_chef_prompt | chat
veg_chain.invoke("어묵")
# %%
final_chain = {"receipe": chef_chain} | veg_chain
final_chain.invoke({"menu": "떡볶이", "receipe": "어묵"})
# %%
final_chain.invoke({"menu": "김치찌개", })
# %%
