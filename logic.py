import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def enhance_email(user_input: str, scenario: str, tone: str, scenario_context: str,language: str) -> str:
    prompt = generate_prompt(user_input, scenario, tone, language)
    if scenario_context:
        messages = [{"role": "system", "content": "You are an email assistant that helps first-generation professionals write clear and well articulated emails."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": f"For some additional context, below is the email we are replying to. Please match the vibe when revising the email draft:\n{scenario_context}"}]
    else:
        messages = [{"role": "system", "content": "You are an email assistant that helps first-generation professionals write clear and well articulated emails."},
            {"role": "user", "content": prompt}]
    # Generate the response using OpenAI's chat completion API

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content


def generate_prompt(user_input: str, scenario: str, tone: str, language: str) -> str:
    return (
        f"Please help improve the following email for a {scenario.replace('_', ' ')} situation. "
        f"Make it sound more {tone}." #and suitable for a professional setting. "
        f"The language should be {language}.\n"
        f"Raw email that needs to be revised: \n{user_input}"

    )
