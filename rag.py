from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import os
from llm import get_llm

def load_split_embeds_stores_pdfs_in_FAISS(folder_path="data/"):
    #Load the PDF documents
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            docs = loader.load()
            documents.extend(docs)

    #Split the documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(documents)

    #Embedding and storing the split documents in FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",cache_folder="./models/minilm")
    vector = FAISS.from_documents(split_docs, embeddings)

    return vector

def get_rag_chain(vector):
    #Retrieve from the vector store
    retriever = vector.as_retriever()

    prompt = PromptTemplate(
        input_variables=["context","input"],
        template="""
        You are an AI assistant. Use the following context to answer the question as clearly and concisely as possible.

        If the answer is not found in the context, respond with: "I don't know from the PDF."

        Context:
        {context}

        Input:
        {input}

        Answer:
        """)

    document_chain = create_stuff_documents_chain(llm = get_llm(),prompt=prompt)
    rag_chain = create_retrieval_chain(retriever=retriever,combine_docs_chain=document_chain)

    return rag_chain


    