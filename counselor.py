from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from retriever import build_vector_store

def get_career_recommendation(student_profile):
    vector_store = build_vector_store()
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)  # Fixed argument name

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    prompt = (
        "Given the student profile:\n"
        f"Skills: {', '.join(student_profile.get('skills', []))}\n"
        f"Interests: {', '.join(student_profile.get('interests', []))}\n"
        f"Aptitude: {', '.join(student_profile.get('aptitude', []))}\n\n"
        "Recommend 2-3 suitable career paths with reasons, relevant courses to take, and expected industry growth."
    )

    result = qa_chain.run(prompt)
    return result
