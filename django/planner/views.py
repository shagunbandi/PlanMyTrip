from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatgpt.prompts import generate_itinerary
from chatgpt.utilities import prompt_chat_gpt
from maps.utilities import google_text_search, update_distance_to_reach
from maps.utilities import travelling_salesmen_problem
from chatgpt.sample.plan_overview import malaga_5_days


@api_view(["POST"])
def PlanOverview(request):
    content = request.data
    number_of_days = content.get("number_of_days", 5)
    country = content.get("country", "")
    circular = content.get("circular", True)
    is_mock = content.get("is_mock", True)
    if is_mock:
        response = malaga_5_days
    else:
        prompt = generate_itinerary(number_of_days, country)
        response = prompt_chat_gpt(prompt)  # Calls Chat GPT Api
        response = enrich_data(response)  # Calls Google Places API
        response = travelling_salesmen_problem(response, 0, circular)
        response = update_distance_to_reach(response)
    return Response(response, 200)


def enrich_data(content: object):
    points = []
    for c in content:
        details = google_text_search(f"{c['name']} in {c['city']}")
        point = c.copy()
        point.update(details)
        points.append(point)
    return points
