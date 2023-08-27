import os 
import gtts # google text-to-speech library
import openai # openai library
from playsound import playsound # to save audio file

# configuration
import creds # script storeing api keys
openai.api_key = creds.OPENAI_API_KEY
openai.api_base = 'https://api.openai.com/v1/chat'

class ChatGPTAPI:
    def __init__(self, system_setting, temperature=0.5, max_tokens=50):
        self.system = {"role": "system", "content": system_setting}
        self.input_list = [self.system]
        self.logs = []
        self.temperature = temperature
        self.max_tokens = max_tokens

    def input_message(self, input_text):
        self.input_list.append({"role": "user", "content": input_text})
        result = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=self.input_list,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        self.logs.append(result)
        self.input_list.append(
            {"role": "assistant", "content": result.choices[0].message.content}
        )
        return self.input_list[-2]["content"], self.input_list[-1]["content"]
    
def text_to_speech(text):
    tts = gtts.gTTS(text)

    # save the audio file
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")
    tts.save("output.mp3")

    # play the audio file
    playsound('output.mp3', True)