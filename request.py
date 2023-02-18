import openai
import api

openai.organization = "org-SdlEoRzHJvM2Inm91szJa9DX"
openai.api_key = api.API_KEY
openai.Model.list()


def make_request(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=2000, temperature=0)
    print(response["choices"][0]["text"])
    return response["choices"][0]["text"]

