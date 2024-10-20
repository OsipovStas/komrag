from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec
import os
import time
from langchain_pinecone import PineconeVectorStore
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def create_rag_chain():
    load_dotenv(".env", override=True)
    model = "gpt-4o-mini-2024-07-18"
    chat = AzureChatOpenAI(model=model, temperature=0, timeout=120)
    embeddings = AzureOpenAIEmbeddings(model="text-embedding-3-small-1", dimensions=768)
    pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
    vectorstore = PineconeVectorStore(index=get_index(pc), embedding=embeddings)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    prompt = hub.pull("rlm/rag-prompt")
    rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | chat
            | StrOutputParser()
    )
    return rag_chain


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_index(pc):
    index_name = "komrag"  # change if desired
    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(index_name).status["ready"]:
            time.sleep(1)

    index = pc.Index(index_name)
    return index
