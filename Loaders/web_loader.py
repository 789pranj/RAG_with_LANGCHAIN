from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt = PromptTemplate(
    template="Write a summary for the following text:\n\n{document}",
    input_variables=["document"]
)

parser = StrOutputParser()

url = 'https://docs.langchain.com/oss/python/integrations/document_loaders'
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({'document': docs[0].page_content})

print(result)
