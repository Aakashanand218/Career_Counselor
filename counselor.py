from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever import build_vector_store

def get_career_recommendation(student_profile):
    vector_store = build_vector_store()
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    prompt = f"""
    Given the student profile:
    Skills: {', '.join(student_profile['skills'])}
    Interests: {', '.join(student_profile['interests'])}
    Aptitude: {', '.join(student_profile['aptitude'])}

    Recommend 2-3 suitable career paths with reasons, relevant courses to take, and expected industry growth.
    """

    result = qa_chain.run(prompt)
    return result
