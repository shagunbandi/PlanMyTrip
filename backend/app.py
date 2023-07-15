from flask import Flask, request
from flask_cors import CORS

from apis import google_distance_matrix, get_chat_gpt_reply
from logic import generate_content
from static.reply.response_with_maps import india_10_days

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def index():
    # return india_10_days
    content = request.json
    number_of_days = content.get("number_of_days")
    country = content.get("country")
    is_mock = content.get("is_mock")
    try:
        prompt = generate_content(number_of_days, country)
        content = get_chat_gpt_reply(prompt=prompt, is_mock=is_mock)
    except Exception as e:
        return {"status": 500, "error": e.args[0]}
    return {
        "status": 200,
        "response": {
            "content": content,
        },
        "prompt": prompt,
    }


@app.route("/maps/distance", methods=["POST"])
def distance_with_place_ids():
    content = request.json
    origin_place_id = content.get("origin_place_id")
    destination_place_id = content.get("destination_place_id")
    mode = content.get("mode", "driving")

    response = google_distance_matrix(
        origin_place_id=origin_place_id,
        destination_place_id=destination_place_id,
        mode=mode,
    )
    return {
        "status": 200,
        "response": response,
    }


@app.route("/")
def not_found():
    return {"status": 404, "message": "Not Found"}
