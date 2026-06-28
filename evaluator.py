import os

from groq import Groq

# API key is read from the GROQ_API_KEY environment variable.
# Set it before running, e.g. (PowerShell):  $env:GROQ_API_KEY = "your-key"
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise RuntimeError(
        "GROQ_API_KEY environment variable is not set. "
        "Create a key at https://console.groq.com and set it, e.g.\n"
        '  PowerShell:  $env:GROQ_API_KEY = "your-key"\n'
        '  bash:        export GROQ_API_KEY="your-key"'
    )

client = Groq(api_key=api_key)


def evaluate_answer(question, answer):

    prompt = f"""
You are a Senior Technical Interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

1. Technical Score (out of 10)
2. Communication Score (out of 10)
3. Strengths
4. Weaknesses
5. Missing Concepts
6. Improved Answer
7. Final Recommendation

Provide detailed feedback.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are an expert interviewer specializing in:

- Python
- SQL
- Machine Learning
- Deep Learning
- NLP
- Generative AI
- RAG
- LangChain

Provide professional interview feedback.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1500
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    print("=" * 70)
    print("INTERVIEW ANSWER EVALUATOR")
    print("=" * 70)

    question = input(
        "\nEnter Interview Question:\n\n"
    )

    answer = input(
        "\nEnter Candidate Answer:\n\n"
    )

    result = evaluate_answer(
        question,
        answer
    )

    print("\n")
    print("=" * 70)
    print("INTERVIEW EVALUATION REPORT")
    print("=" * 70)
    print(result)