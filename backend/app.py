from flask import Flask, request
from flask_cors import CORS

from apis import google_maps, chat_gpt
from logic import gpt_prompts
from static.reply.response_with_maps import amsterdam_3_days

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def index():
    content = request.json
    number_of_days = content.get("number_of_days")
    country = content.get("country")
    is_mock = content.get("is_mock")
    if is_mock:
        return amsterdam_3_days

    try:
        prompt = gpt_prompts.generate_content(number_of_days, country)
        content = chat_gpt.get_chat_gpt_reply(prompt=prompt)
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

    response = google_maps.google_distance_matrix(
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
