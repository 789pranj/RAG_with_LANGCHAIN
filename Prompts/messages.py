from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


message = [
    SystemMessage(content='You are the helpful advance ai assistant'),
    HumanMessage(content='Tell me about the LangChain in 2 lines')
]

result = model.invoke(message)

message.append(AIMessage(content=result.content))

print(message)
