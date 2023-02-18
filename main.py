from request import make_request
from edit_request import edit_request
from text_to_speech import text_to_speech

def main():
    print("|---------------------------------------------------------------------------------|")
    input_no = ""
    user_question = input("Do you want to write prompt for AI? y/n or press x for exit  ")
    while input_no != "no":
        print("|---------------------------------------------------------------------------------|")
        if user_question == "y":
            print("if you want to exit writing prompts for AI: press n or press x for exit applications  ")
            user_prompt = input("Insert Prompt for AI: ")
            if user_prompt == "x":
                exit()
            elif user_prompt == "n":
                user_question = "n"
            else:
                text_to_speech(make_request(user_prompt))
        elif user_question == "n":
            input_no = "no"
        elif user_question == "x":
            exit()
    print("|---------------------------------------------------------------------------------|")
    user_prompt_2 = input("Do you want to edit text? y/n or press x for exit  ")
    while True:
        print("|---------------------------------------------------------------------------------|")
        if user_prompt_2 == "y":
            print("if you want to exit text editing: press n or press x for exit applications  ")
            user_prompt_3 = input("Insert text to edit:  ")
            if user_prompt_3 == "n":
                main()
            elif user_prompt_3 == "x":
                exit()
            else:
                user_prompt_4 = input("Insert edit instructions for AI: ")
                edit_request(user_prompt_3, user_prompt_4)
        elif user_prompt_2 == "n":
            main()
            exit()
        elif user_prompt_2 == "x":
            exit()

if __name__ == '__main__':
    main()


