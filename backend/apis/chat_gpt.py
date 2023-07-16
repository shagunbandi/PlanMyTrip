# imports
import openai  # for OpenAI API calls
import json
from apis import google_maps
from logic import shortest_path, distance_to_reach
from static.reply.suggestions import india_5_days


def get_chat_gpt_reply(prompt):
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=prompt,
    #     temperature=0.5,
    #     n=1,
    #     stop=None,
    #     max_tokens=512,
    # )
    # content = response.choices[0].text.strip()
    # content_json = json.loads(content)

    content_json = india_5_days

    points = []
    for c in content_json:
        details = google_maps.google_text_search(f"{c['name']} in {c['city']}")
        point = c.copy()
        point.update(details)
        points.append(point)

    points = shortest_path.travelling_salesmen_problem(points, 0, True)
    points = distance_to_reach.update_distance_to_reach(points)
    return points
