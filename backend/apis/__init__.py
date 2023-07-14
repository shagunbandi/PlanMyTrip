import requests
import os

# imports
import openai  # for OpenAI API calls
import time  # for measuring time duration of API calls
import os
import json
from static.reply.suggestions import suggestion_3 as suggestion


openai.api_key = os.getenv("OPENAI_API_KEY")


API_KEY = os.getenv("MAP_API_KEY")


def get_chat_gpt_reply(prompt, is_mock=True):
    # record the time before the request is sent
    start_time = time.time()
    content_json = {}
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
    # End time
    response_time = time.time() - start_time

    return response_time, detailed_content


def google_text_search(query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "key": API_KEY,
    }

    response = requests.request("GET", url, params=params)
    response_json = response.json()
    first_result = response_json["results"][0]
    return {
        "location": first_result["geometry"]["location"],
        "icon": first_result["icon"],
        "name": first_result["name"],
        "photos": first_result["photos"],
        "place_id": first_result["place_id"],
        "rating": first_result["rating"],
        "user_ratings_total": first_result["user_ratings_total"],
    }


def google_distance_matrix(origin, destination, mode):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "mode": mode,
        "key": API_KEY,
    }

    response = requests.request("GET", url, params=params)
    response_json = response.json()
    return {
        "origin_address": response_json["origin_addresses"][0],
        "destination_address": response_json["destination_addresses"][0],
        "distance_in_meters": response_json["rows"][0]["elements"][0]["distance"][
            "value"
        ],
        "time_in_minutes": response_json["rows"][0]["elements"][0]["duration"]["value"],
    }
