def generate_content(number_of_days, country):
    return "".join(
        [
            "Suggest me {}-day trip to {}. Do not include any explanations, only provide a  RFC8259 compliant JSON response in a single line following this format without deviation.\n".format(
                number_of_days, country
            ),
            '[{"day_number": "nth day"',
            '"time": "number of hours to complete the activity"',
            '"name": "name of the place"',
            '"city": "a major city near the location"'
            '"category": "destination type"'
            "'"
            "}]",
        ]
    )
