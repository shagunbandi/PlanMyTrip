# imports
import openai  # for OpenAI API calls
import time  # for measuring time duration of API calls
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")


def call_gpt(prompt):
    # record the time before the request is sent
    start_time = time.time()

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        n=1,
        stop=None,
        max_tokens=1024,
    )
    content = response.choices[0].text.strip()
    content_json = json.loads(content)
    # End time
    response_time = time.time() - start_time

    return response_time, content_json
