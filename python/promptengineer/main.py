# pip install openai

import openai
import os
openai.api_key = os.getenv("OPENAIKEY") #set env value (echo %OPENAIKEY%)

def prompt_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0
    )
    return response.choices[0].message['content']


response=prompt_content("what is capital of India")
print(response)