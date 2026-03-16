from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generater the short and simple notes for the following. \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answer from the following. \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merger the provided notoes and quiz in to the single document \n notes --> {notes} \n quiz --> {quiz}',
    input_variables=['notes', 'quiz']
)

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model | parser,
        'quiz' : prompt2 | model | parser
    }
)

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """Reinforcement learning is an area of machine learning where an agent learns to make decisions by interacting with an environment. Instead of being given explicit instructions or labeled data, the agent learns through trial and error and receives feedback in the form of rewards or penalties. Over time, the agent improves its strategy, known as a policy, to maximize cumulative rewards. The environment is typically modeled using states, actions, and rewards, and the agent must learn how to transition between states while choosing the best possible actions.
A key concept in reinforcement learning is the balance between exploration and exploitation. Exploration means trying new actions to discover their potential rewards, while exploitation means using known actions that already yield the highest rewards. Finding the right balance is crucial for optimal learning.
Reinforcement learning techniques include value-based methods like Q-learning, policy-based methods, and actor-critic approaches that combine both. These methods allow the agent to estimate the usefulness of actions and policies in different states.
Reinforcement learning has practical applications in robotics, game-playing systems, autonomous vehicles, resource management, and natural language processing. It has achieved notable success in advanced systems such as AlphaGo and self-learning control systems. Despite its success, reinforcement learning can be computationally expensive and challenging due to delayed rewards, large state spaces, and instability in training."""

output = chain.invoke({'text': text})
print(output)

chain.get_graph().print_ascii()
