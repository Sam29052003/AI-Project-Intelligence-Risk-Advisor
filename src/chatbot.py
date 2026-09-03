def generate_answer(question):

    documents = retrieve_documents(question)

    context = "\n\n".join(documents)

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    prompt = f"""
You are an AI Project Intelligence & Risk Advisor.

Answer the question using ONLY the information provided
in the project document context.

If the answer is not available in the uploaded documents,
say exactly:

Information not found in the uploaded project documents.

PROJECT DOCUMENT CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    response = llm.invoke(prompt)

    content = response.content

    if isinstance(content, list):
        answer = ""

        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                answer += item.get("text", "")

        return answer

    return content