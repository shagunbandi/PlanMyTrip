import requests
import os

API_KEY = os.getenv("MAP_API_KEY")


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
