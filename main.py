import speech_recognition as sr # speech recognition library
import pyttsx3 # text-to-speech library
import function # class function to interact with Chat GPT API

# initialize speech recognizer and text-to-speech function
r = sr.Recognizer()
tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty("voice", voices[0].id) # 0: English David, 1: English Zira, 2: Japanese Haruka


# define name of the assistant and system setting
assistant_name = "Haruka"
system_setting = f"You are a streamer and your name is {assistant_name}. You like playing video games and siging. You were created by Dr. Hopkins. You always say Meow at the end."

# import class function and initialize system setting
api = function.ChatGPTAPI(system_setting=system_setting)

while True:
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=1.0)
        audio = r.listen(source)
    try:
        # recognize speech
        text = r.recognize_google(audio, language="en-EN")

        # send speech to api and receive response
        text_user, text_chatgpt = api.input_message(text)
        print('[User]: '+text_user)
        print(f'[{assistant_name}]: {text_chatgpt}')

        # make request to google to get synthesis
        text = text_user + text_chatgpt;
        function.text_to_speech(text)


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))