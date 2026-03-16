from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="Generate the tweet about the topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate the linkedIn post about the topic - {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

parellel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedIn' : RunnableSequence(prompt2, model, parser)
})

result = parellel_chain.invoke({'topic': 'AI'})

print(result)