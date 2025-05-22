import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def enhance_email(user_input: str, scenario: str, tone: str, language: str) -> str:
    prompt = generate_prompt(user_input, scenario, tone, language)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an email assistant that helps first-generation professionals write clear, confident, and professional emails."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content


def generate_prompt(user_input: str, scenario: str, tone: str, language: str) -> str:
    return (
        f"Please help improve the following email for a {scenario.replace('_', ' ')} situation. "
        f"Make it sound more {tone} and suitable for a professional setting. "
        f"The language should be {language}.\n\n"
        f"Raw email: \n{user_input}"
    )
