# imports
import openai  # for OpenAI API calls
import json
from static.reply.response_with_maps import india_10_days as response_with_maps
from static.reply.suggestions import india_5_days
from apis.google_maps import google_text_search

from logic.shortest_path import travelling_salesmen_problem


def get_chat_gpt_reply(prompt, is_mock=True):
    # content_json = []
    # if not is_mock:
    #     response = openai.Completion.create(
    #         engine="text-davinci-003",
    #         prompt=prompt,
    #         temperature=0.5,
    #         n=1,
    #         stop=None,
    #         max_tokens=1024,
    #     )
    #     content = response.choices[0].text.strip()
    #     content_json = json.loads(content)
    # else:
    #     content_json = india_5_days

    # detailed_content = [
    #     {
    #         "day_number": c["day_number"],
    #         "time": c["time"],
    #         "gpt_name": c["name"],
    #         "gpt_city": c["city"],
    #         "category": c["category"],
    #         "details": google_text_search(f"{c['name']} in {c['city']}"),
    #     }
    #     for c in content_json
    # ]

    detailed_content = response_with_maps["response"]["content"]
    sorted_content = travelling_salesmen_problem(detailed_content, 3, False)

    return sorted_content
