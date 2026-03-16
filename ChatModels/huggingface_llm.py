from langchain_huggingface.chat_models import ChatHuggingFace
from langchain_core.messages import HumanMessage
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

model_name = "HuggingFaceH4/zephyr-7b-beta"

# Create a HuggingFace pipeline first
chat_pipeline = pipeline(
    "text-generation",
    model=model_name,
    device=0  # Use -1 for CPU
)

# Pass it to ChatHuggingFace via llm parameter
llm = ChatHuggingFace(llm=chat_pipeline)

messages = [HumanMessage(content="What is the capital of France?")]
response = llm.invoke(messages)
print(response.content)
