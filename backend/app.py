import json

from flask import Flask, redirect, render_template, request, url_for
from flask import jsonify
from logic.call_gpt import call_gpt
from logic.suggestions import generate_content
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        content = request.json
        number_of_days = content.get("number_of_days")
        country = content.get("country")
        is_prompt = content.get("is_prompt")
        prompt = generate_content(number_of_days, country)
        if True:
            return {
                "number_of_days": number_of_days,
                "country": country,
                "is_prompt": is_prompt,
                "prompt": prompt,
                "response": {
                    "content": [
                        {
                            "category": "Adventure",
                            "day_number": "1st day",
                            "major_city": "Paro",
                            "name": "Tiger's Nest",
                            "time": "9am",
                        },
                        {
                            "category": "Historic",
                            "day_number": "1st day",
                            "major_city": "Agra",
                            "name": "Taj Mahal",
                            "time": "3pm",
                        },
                        {
                            "category": "Adventure",
                            "day_number": "2nd day",
                            "major_city": "Goa",
                            "name": "Dudhsagar Falls",
                            "time": "9am",
                        },
                        {
                            "category": "Historic",
                            "day_number": "2nd day",
                            "major_city": "Jodhpur",
                            "name": "Mehrangarh Fort",
                            "time": "3pm",
                        },
                        {
                            "category": "Cultural",
                            "day_number": "2nd day",
                            "major_city": "Kochi",
                            "name": "Kathakali Performance",
                            "time": "6pm",
                        },
                    ],
                    "time_taken": "24.55s",
                },
                "status": 200,
            }
        else:
            response_time, content = call_gpt(prompt=prompt)
            return {
                "status": 200,
                "response": {
                    "time_taken": f"{response_time:.2f}s",
                    "content": content,
                },
                "prompt": prompt,
            }
    return {"status": 201, "country": country, "number_of_days": number_of_days}


@app.route("/health", methods=("GET", "POST"))
def health():
    return {"status": 201}


@app.route("/")
def not_found():
    return {"status": 404, "message": "Not Found"}
