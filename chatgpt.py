import os
import sys
import time
import openai

systemPrompt = { "role": "system", "content": "You are a helpful assistant." }

openai.api_key = os.getenv("OPENAI_API_KEY")

data = []

def get_chatgpt_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:
        data.append({"role": "assistant", "content": incoming_msg})
    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""