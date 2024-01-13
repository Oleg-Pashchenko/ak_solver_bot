import time

import openai
import dotenv
import os

dotenv.load_dotenv()

client = openai.AsyncOpenAI(api_key=os.getenv('OPENAI_KEY'))


async def run(messages):
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=messages)
    return response.choices[0].message.content


