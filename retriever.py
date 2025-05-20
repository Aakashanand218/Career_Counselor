from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import os

def build_vector_store(file_path='data/career_knowledge_base.txt'):
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    docs = [Document(page_content=chunk) for chunk in CharacterTextSplitter(chunk_size=300, chunk_overlap=50).split_text(raw_text)]

    embeddings = OpenAIEmbeddings(openai_api_key="YOUR_API_KEY")
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store
