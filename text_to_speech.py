import pyttsx3

engine = pyttsx3.init()
def text_to_speech(text_input):
    engine.say(text_input)
    return engine.runAndWait()