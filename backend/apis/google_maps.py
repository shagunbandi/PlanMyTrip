import requests
import os

API_KEY = os.getenv("MAP_API_KEY")


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
        "icon": first_result.get("icon", None),
        "name": first_result.get("name", None),
        "photos": first_result.get("photos", None),
        "place_id": first_result.get("place_id", None),
        "rating": first_result.get("rating", None),
        "user_ratings_total": first_result.get("user_ratings_total", None),
    }


def google_distance_matrix(
    origin_place_id: str, destination_place_id: str, mode="driving"
):
    # https://developers.google.com/maps/documentation/distance-matrix/distance-matrix
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": "place_id:" + origin_place_id,
        "destinations": "place_id:" + destination_place_id,
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
        "duration_in_mins": response_json["rows"][0]["elements"][0]["duration"][
            "value"
        ],
    }
