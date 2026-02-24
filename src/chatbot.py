import chromadb
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def load_collection():
    client = chromadb.PersistentClient(path="data/chroma_db")
    collection = client.get_collection(name="faq")
    return collection


def search_faq(collection, user_question, n_results=3):
    results = collection.query(
        query_texts=[user_question],
        n_results=n_results
    )

    return results

def build_context(results):
    context = ""
    for i in range(len(results['documents'][0])):
        question = results['documents'][0][i]
        answer = results['metadatas'][0][i]['answer']
        context += f"Q: {question}\nA: {answer}\n\n"
    return context

def ask_chatbot(collection, llm, user_question):
    # search chromDB for similar faqs
    results = search_faq(collection, user_question)
    
    # build content from results
    context = build_context(results)

    # create prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an FAQ chatbot for Amazon Electronics products.
        Use the following FAQ information to answer the question.
        If the answer is not in the FAQ, say you do not know.
        
        FAQ Context:
        {context}
        
        User Question: {question}
        
        Answer:"""
    )

    # generate response
    chain = prompt | llm
    response = chain.invoke({
        "context": context,
        "question": user_question
    })

    return response

