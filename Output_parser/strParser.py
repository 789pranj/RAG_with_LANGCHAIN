from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

templete1 = PromptTemplate(
    template='Write a detailed report about {topic}',
    input_variables=['topic']
)

templete2 = PromptTemplate(
    template='Write the 5 line summary on the following {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = templete1 | model | templete2 | model | parser

result = chain.invoke({'topic': 'Black hole'})

print(result)


# prompt1 = templete1.invoke({'topic': 'Black Hole'})
# result = model.invoke(prompt1)

# prompt2 = templete2.invoke({'text': result.content})
# final_result = model.invoke(prompt2)

# print(final_result)

