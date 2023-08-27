# Speech-to-Text ChatGPT

## About
In ChatGPT, you can write a prompt and get a response in text. Would it be nice if we can speak into a mic and get a voice response?
I combined ChatGPT API, Google's speech-to-text library, and text-to-speech library to create a virtual assistan that you can interact with your own voice and with a character of your own setting.

## How it works

### 1. Preparation
Create a virtual environment in vscode and activate it.
```bash
virtualenv venv --python=python3.9
venv\Scripts\activate
```
Install libraries in `requirements.txt`


In `creds.py`, insert your ChatGPT API key and Google speech-to-text API key.

### 2. Settings

Decide the name of your virtual assistant, a character and how he/she acts in below [`main.py`].
```bash
# define name of the assistant and system setting
assistant_name = "Haruka"
system_setting = f"You are a streamer and your name is {assistant_name}. You like playing video games and siging. You were created by Dr. Hopkins. You always say Meow at the end."
```

### 3. Run
Run `main.py`.

### 4. Speech
When you see "Say something!" in the terminal, speak to your microphone. And in a few seconds, your virtual assistant will talk back!

![alt text](https://github.com/wideflat/chatgpt-speech-to-text-app/blob/main/images/image1.png)

...END
