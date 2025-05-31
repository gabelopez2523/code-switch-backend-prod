import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def enhance_email(user_input: str, tone: str, scenario_context: str,language: str) -> str:
    prompt = generate_prompt(user_input, tone, language)

    system_prompt = '''    
You are a helpful email assistant that specializes in rewriting and enhancing professional emails for Gen-Z (18 to 26), first-generation college graduates entering or new to the professional workforce. You take into account both tone preferences (casual or professional) and any provided context, such as emails the user is replying to. When context is available, use it to craft a relevant, natural-sounding response that addresses the original message appropriately.
Focus on making the tone confident, clear, and appropriately professional without sounding overly formal or stiff. Use natural phrasing and modern email etiquette. If the user prompt mentions confirming, requesting, following up, or responding, pay close attention to the action and match the tone accordingly.
When replying to legal, financial, or technical messages, maintain accuracy and clarity, and match any required precision. Always keep the email structure clean: greet if appropriate, provide the message body, and close with a friendly but professional sign-off.
If the user includes previous email content as context, incorporate relevant details directly to ensure the reply feels cohesive and directly responsive.
                '''

    if scenario_context:
        messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"role": "user", "content": f"This is the email we are replying to which you will use as context:\n{scenario_context}"}]
    else:
        messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}]
    # Generate the response using OpenAI's chat completion API

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1.0
    )

    return response.choices[0].message.content


def generate_prompt(user_input: str, tone: str, language: str) -> str:
    return (
        #f"Please help improve the following email for a {scenario.replace('_', ' ')} situation. " currently not used
        f"Please revise the following email to sound more {tone}. The language should be in {language}." #and suitable for a professional setting. "
        f"Email to revise:: \n{user_input}"

    )
