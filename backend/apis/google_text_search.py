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
        "icon": first_result["icon"],
        "name": first_result["name"],
        "photos": first_result["photos"],
        "place_id": first_result["place_id"],
        "rating": first_result["rating"],
        "user_ratings_total": first_result["user_ratings_total"],
    }
