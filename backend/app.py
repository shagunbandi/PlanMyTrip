from flask import Flask, request
from flask_cors import CORS

from apis import google_distance_matrix, google_text_search, get_chat_gpt_reply
from logic.gpt_questions import generate_content
from static.reply.response_with_maps import response_1

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def index():
    return response_1
    # content = request.json
    # number_of_days = content.get("number_of_days")
    # country = content.get("country")
    # is_mock = content.get("is_mock")
    # prompt = generate_content(number_of_days, country)
    # response_time, content = get_chat_gpt_reply(prompt=prompt, is_mock=is_mock)
    # return {
    #     "status": 200,
    #     "response": {
    #         "time_taken": f"{response_time:.2f}s",
    #         "content": content,
    #     },
    #     "prompt": prompt,
    # }


@app.route("/maps/distance", methods=["POST"])
def distance_with_place_ids():
    content = request.json
    origin = content.get("origin")
    destination = content.get("destination")
    mode = content.get("mode", "driving")

    response = google_distance_matrix(origin=origin, destination=destination, mode=mode)
    return {
        "status": 200,
        "response": response,
    }


@app.route("/maps/textsearch", methods=["POST"])
def text_search():
    content = request.json
    query = content.get("query")

    response = google_text_search(query=query)
    return {
        "status": 200,
        "response": response,
    }


@app.route("/health", methods=("GET", "POST"))
def health():
    return {"status": 201}


@app.route("/")
def not_found():
    return {"status": 404, "message": "Not Found"}
