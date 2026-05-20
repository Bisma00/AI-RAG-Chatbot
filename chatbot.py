import os

from dotenv import load_dotenv

from openai import OpenAI

from retrieval import retrieve_context


load_dotenv()


client = OpenAI(

    base_url="https://openrouter.ai/api/v1",

    api_key=os.getenv("OPENROUTER_API_KEY")
)


def build_prompt(query, context):

    prompt = f"""
You are an internal company AI assistant.

Answer the employee question ONLY using the provided context.

If the answer is not found in the context, say:
"I could not find relevant information in the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

    return prompt


def generate_response(query):

    retrieved_docs = retrieve_context(query)

    context = "\n\n".join(

        [doc.page_content for doc in retrieved_docs]
    )

    prompt = build_prompt(query, context)

    try:

        response = client.chat.completions.create(

            model="openai/gpt-oss-20b:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return answer, retrieved_docs

    except Exception as e:

        error_message = f"Error generating response: {str(e)}"

        return error_message, retrieved_docs

if __name__ == "__main__":

    query = "What is the company leave policy?"

    response, sources = generate_response(query)

    print("\nChatbot Response:\n")

    print(response)