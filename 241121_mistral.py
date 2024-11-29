from dotenv import load_dotenv
import os
from mistralai import Mistral
# pip install python-dotenv
# pip install mistralai
# code ./

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)


model = "mistral-large-latest"
custom_messages = [
    {
        "role": "user",
        "content": "[다음]에 표현된 감정(긍정, 중립, 부정)을 식별하고 분류해줘. [생성형AI의 기능은 매우 놀랍습니다!!] ",
    },
    {
        "role": "user",
        "content": "고양이: 동물 <br> 오렌지: 과일 <br> 토마토: 채소 <br> 비둘기: "
    }
]

chat_response = client.chat.complete(
    model=model,
    messages=custom_messages
)
print(chat_response)

print(chat_response.choices[0].message.content)
