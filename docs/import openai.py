

import os
from openai import OpenAI # pip install openai
from keys import open_ai_api_key # you must enter your OpenAI API key in a file called keys.py

client = OpenAI(
    api_key=open_ai_api_key
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # This first message is prob not needed but can be useful in some cases, maybe you want the AI to act like a HCI researcher.
        {"role": "system", "content": "You are a helpful assistant."},   

        # this is the actual question
        {
            "role": "user",
            "content": "Give me the ingredients and instructions for this URL: http://www.food.com/recipe/greek-quinoa-salad-with-avocados-469270 as a Python dictionary.",
        }
    ]
)

result = completion.choices[0].message.content
print(result)
