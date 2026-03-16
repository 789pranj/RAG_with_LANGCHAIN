from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of an anime character.\n {format_instruction}",
    partial_variables={"format_instruction": parser.get_format_instructions()},
    input_variables=[] 
)

chain = template | model | parser

result = chain.invoke({})

print(result)


# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content) # pyright: ignore[reportArgumentType]

# print(final_result)

