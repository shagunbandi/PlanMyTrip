from flask import Flask, request
from flask_cors import CORS

from apis import google_distance_matrix, google_text_search, get_chat_gpt_reply
from logic.gpt_questions import generate_content
from static.reply.response_with_maps import india_10_days as response

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def index():
    return response
    # content = request.json
    # number_of_days = content.get("number_of_days")
    # country = content.get("country")
    # is_mock = content.get("is_mock")
    # prompt = generate_content(number_of_days, country)
    # content = get_chat_gpt_reply(prompt=prompt, is_mock=is_mock)
    # return {
    #     "status": 200,
    #     "response": {
    #         "content": content,
    #     },
    #     "prompt": prompt,
    # }


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
