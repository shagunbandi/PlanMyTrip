import json
import openai  # for OpenAI API calls


def generate_prompt_json(question: str, json_response_format: json):
    return "{}. Do not include any explanations, only provide a  RFC8259 compliant JSON response in a single line following this format without deviation.\n{}".format(
        question, json.dumps(json_response_format)
    )


def prompt_chat_gpt(
    prompt: str,
    engine="text-davinci-003",
    temperature=0.5,
    n=1,
    stop=None,
    max_tokens=1024,
    **kwargs
):
    response = openai.Completion.create(
        prompt=prompt,
        engine=engine,
        temperature=temperature,
        n=n,
        stop=stop,
        max_tokens=max_tokens,
        **kwargs
    )
    content = response.choices[0].text.strip()
    return json.loads(content)
