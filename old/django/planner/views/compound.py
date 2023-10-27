from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatgpt.prompts import generate_itinerary
from chatgpt.utilities import prompt_chat_gpt
from maps.utilities import google_text_search, update_distance_to_reach
from maps.utilities import travelling_salesmen_problem
from chatgpt.sample.plan_overview import malaga_5_days
from planner.serializers import (
    CreateItineraryCompoundSerializer,
    ItineraryElementSerializer,
    ItineraryCompoundSerializer,
)
from planner.models import ItineraryElement, ItineraryCompound


@csrf_exempt
@api_view(["GET"])
def fetch_compound(request):
    id = request.GET.get("id", None)
    compound = ItineraryCompound.objects.filter(id=id).first()
    if not compound:
        return Response(status=404)
    return Response(ItineraryCompoundSerializer(instance=compound).data, 200)


@csrf_exempt
@api_view(["GET"])
def fetch_all_compound(request):
    all_compounds = ItineraryCompound.objects.all()

    return Response(
        [
            ItineraryCompoundSerializer(instance=compound).data
            for compound in all_compounds
        ],
        200,
    )


@csrf_exempt
@api_view(["POST"])
def create_compound(request):
    content = request.data
    CreateItineraryCompoundSerializer(data=content).is_valid()
    name = content.get("name")
    place = content.get("place")
    number_of_days = content.get("number_of_days")
    circular = content.get("circular", True)
    is_mock = content.get("is_mock", True)
    note = content.get("note", "")
    if is_mock:
        response = malaga_5_days
    else:
        prompt = generate_itinerary(number_of_days, place)
        response = prompt_chat_gpt(prompt)  # Calls Chat GPT Api
        response = _enrich_data(response)  # Calls Google Places API
        response = travelling_salesmen_problem(response, 0, circular)
        response = update_distance_to_reach(response)

    # Make it atomic
    compound = ItineraryCompound(name=name)
    compound.save()
    response = [createFromJson(json, compound) for json in response]
    response = [ItineraryElementSerializer(element).data for element in response]
    return Response(
        {"compound_name": compound.name, "compound_elements": response}, 200
    )


# Helpers
def createFromJson(json, compound):
    element = ItineraryElement(
        compound=compound,
        place_id=json["place_id"],
        name=json["name"],
        city=json["city"],
        category=json["category"],
        activity_time_in_mins=json["time"],
        rating_value=json["rating"],
        rating_count=json["user_ratings_total"],
        duration_in_mins=json["duration_in_mins"],
        distance_in_meters=json["distance_in_meters"],
        latitude=json["location"]["lat"],
        longitude=json["location"]["lng"],
        nth_day=1,
        activity_number=1,
    )
    element.save()
    return element


def _enrich_data(content: object):
    points = []
    for c in content:
        details = google_text_search(f"{c['name']} in {c['city']}")
        point = c.copy()
        point.update(details)
        points.append(point)
    return points
