# imports
import openai  # for OpenAI API calls
import json
from static.reply.suggestions import suggestion_4 as suggestion
from apis.google_maps import google_text_search


def get_chat_gpt_reply(prompt, is_mock=True):
    content_json = []
    if not is_mock:
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
    else:
        content_json = suggestion

    detailed_content = [
        {
            "day_number": c["day_number"],
            "time": c["time"],
            "gpt_name": c["name"],
            "gpt_city": c["city"],
            "category": c["category"],
            "details": google_text_search(f"{c['name']} in {c['city']}"),
        }
        for c in content_json
    ]

    return detailed_content
