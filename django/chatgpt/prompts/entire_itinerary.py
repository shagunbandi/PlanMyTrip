from chatgpt.utilities import generate_prompt_json


def generate_itinerary(number_of_days, country):
    return generate_prompt_json(
        question="Suggest me {}-day trip to {}.".format(number_of_days, country),
        json_response_format=[
            {
                "day_number": "nth_day",
                "time": "number of hours to complete the activity",
                "name": "name of the place",
                "city": "a major city near the location",
                "category": "destination type",
            }
        ],
    )
