from flask import Flask
import json
import time
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/testing')
def hello_aq():
    return 'Hello, A!'

@app.route('/tts')
def tts():
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': '7765c7135f75468934b42a29f33461d7',
        'Content-Type': 'application/json',
    }

    json_data = {
        'text': 'Hai nama saya Dicky, saya sedang membuat AI dengan elevenlabs.io',
    }

    response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB', headers=headers, json=json_data)

    with open('prompt_response_new.mp3', 'wb') as f:
        f.write(response.content)
        # print(response.content)
    
    return response