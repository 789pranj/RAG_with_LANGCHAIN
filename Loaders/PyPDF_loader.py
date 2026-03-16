from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('SCM.pdf')

docs = loader.load()

print(len(docs))