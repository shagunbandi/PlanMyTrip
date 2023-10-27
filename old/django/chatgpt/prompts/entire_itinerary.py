from chatgpt.utilities import generate_prompt_json


def generate_itinerary(number_of_days, country):
    return generate_prompt_json(
        question="Suggest me {}-day trip to {}.".format(number_of_days, country),
        json_response_format=[
            {
                "day_number": "integer field - nth_day",
                "time": "integer field - number of minutes to complete the activity",
                "name": "string field - name of the place",
                "city": "string field - a major city near the location",
                "category": "string field - destination type",
            }
        ],
    )
