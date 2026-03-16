from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Artificial Intelligence (AI) has evolved rapidly over the past decade, transforming industries, enhancing automation, and reshaping the way humans interact with technology. At its core, AI aims to enable machines to think, learn, and make decisions in ways that resemble human intelligence. With advancements in machine learning, natural language processing (NLP), and neural networks, AI systems have become capable of understanding speech, recognizing images, predicting user behavior, and even generating human-like content.

One emerging trend within the AI ecosystem is the rise of Large Language Models (LLMs), such as GPT, LLaMA, and others. These models are trained on massive datasets and are capable of understanding context, generating content, answering queries, reasoning, and assisting with problem-solving. However, using raw LLMs directly can sometimes be limiting because they lack structured workflow logic, external knowledge retrieval, and execution ability beyond generating text. This is where LangChain plays a significant role.

LangChain is a framework designed to enhance and extend the capabilities of language models. Instead of treating LLMs as standalone tools, LangChain builds an ecosystem where these models can interact with external data sources, APIs, knowledge bases, and memory. This creates more intelligent, context-aware, and task-specific AI applications.

One of the key strengths of LangChain is its support for Retrieval-Augmented Generation (RAG). With RAG, a model is not limited to what it was trained on—it can fetch additional information from documents, databases, or online sources. This ensures that answers are more accurate, updated, and aligned with real-world data. Applications like AI chatbots, customer support assistants, and research tools often use LangChain-powered RAG pipelines to improve performance.

LangChain also enables agents—LLM-powered systems that can reason, make decisions, and perform actions. These agents can use tools such as search engines, calculators, and web scrapers. Instead of only generating text, they can execute complex workflows such as scheduling, database queries, or automation tasks. For example, an AI assistant built using LangChain can check a calendar, send an email, and generate a meeting summary—all autonomously.

Another useful feature of LangChain is the concept of memory. Traditional AI models treat each request independently, but LangChain allows them to store and recall conversational context. This makes interactions more personalized and human-like, which is especially valuable in applications like therapy bots, learning assistants, and personalized recommendation systems.

Developers prefer LangChain because it provides modular components, flexibility with multiple LLMs, and seamless integration with vector databases like Pinecone, ChromaDB, and FAISS. This makes it an essential tool for building scalable and production-ready AI applications.

In summary, AI and LangChain together represent a major leap in intelligent automation. While AI provides the cognitive engine, LangChain provides structure, connectivity, and functionality to build advanced systems. As adoption increases, the combination of LLMs and LangChain will likely power the next generation of smart applications, bringing AI closer to real human-like interaction and decision-making.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

result = splitter.split_text(text)

print(len(result))
print(result) 