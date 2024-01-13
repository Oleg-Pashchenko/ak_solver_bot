import time

import openai
import dotenv
import os

dotenv.load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_KEY'))


def run(question: str):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {'role': 'system', 'content': "Отвечай на вопрос"},
           # {"role": "system", "content": open('context/test.txt', 'r', encoding='UTF-8').read()},
            {"role": "user", "content": question}
        ])
    return response.choices[0].message.content


