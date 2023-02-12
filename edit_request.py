import openai
import api

openai.api_key = api.API_KEY

def edit_request(original_text, user_edit):
    edited_response = openai.Edit.create(model="text-davinci-edit-001", input=original_text, instruction=user_edit)
    print(edited_response["choices"][0]["text"])
