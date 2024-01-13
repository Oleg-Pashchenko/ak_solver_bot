import time

import openai
import dotenv
import os

dotenv.load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_KEY'))


def run(messages):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages)
    return response.choices[0].message.content


