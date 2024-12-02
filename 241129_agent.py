# %%
from langchain_experimental.tools import PythonAstREPLTool
from langchain.agents import AgentType, Tool, initialize_agent
from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0,
)

python_tool = PythonAstREPLTool()
# %%
tools = [
    Tool(
        name="python_REPL",
        func=python_tool.run,
        description="A Python shell. Use this to execute Python commands. Input should be a valid Python command. If you want to see the output of a value, you should print it."
    )
]

# Initialize the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    api_key="MISTRAL_API_KEY"
)

# agent.run(
#     "파이썬 대표적인 그래프 세 개 그려서 .png 파일로 저장해줘. 그리고 저장하는 파이썬 코드도 .py 파일로 저장해줘. matplotlib 가 설치되어 있어.")

# %%

# agent.run("생성형AI를 활용한 기본 교육후 프로젝트를 위한 기획서 초안을 한국어로 작성해줘. 프로젝트는 실생활에서 유용한 서비스를 제공하는 챗봇형태의 어플리케이션을 개발하는 거야. 어플리케이션의 세부 내용이 잘 표현될 수 있도록 자세하게 작성해줘. 프로젝트의 목적, 목표, 기대효과, 기능, 기술스택, 개발일정, 개발자 역할 등을 포함해줘. 각각의 항목마다 슬라이드를 작성해줘. 각 슬라이드에는 해당 항목의 내용이 잘 드러날 수 있도록 설명을 자세히 적어줘. 각 슬라이드의 제목은 해당 항목의 이름으로 해줘. 마지막으로 생성한 기획서를 파이썬을 이용해서 파워포인트 형식의 plan2.pptx 파일로 저장해줘. ")

# %%

# agent.run("스트림릿과 MistralAI 를 이용해서 사용자 질문에 답변하는 챗팅 기능을 하는 웹앱을 생성해.
#           채팅기능
#           파이썬코드로 작성하고, 작성한 코드를 chat.py 파이썬 파일로 저장해줘. streamlit, MistralAI 라이브러리가 설치되어 있어.       ")

# agent.run("with streamlit and MistralI, create a web app that can chat with users and answer questions that are related to menu and recipes of a Korean fine dining restaurant. The web app should have a chat interface where users can ask questions and get responses. create python .py file and save it as '241129_app.py'. streamlit and MistralAI are installed.")
