from IPython.display import Audio, display
import requests

from flask import Flask

app = Flask(__name__)

def tts(val):
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': '7765c7135f75468934b42a29f33461d7',
        'Content-Type': 'application/json',
    }

    json_data = {
        'text': val,
    }

    response = requests.post('https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB', headers=headers, json=json_data)

    with open('prompt_response_new.mp3', 'wb') as f:
        f.write(response.content)
        # print(response.content)
    
    return response

    # prompt_response_speech = "prompt_response.mp3"
    # display(Audio(prompt_response_speech, autoplay=True))


@app.route('/')
def runTts():
    tts('halo apa kabar Bro!?')

if __name__ == '__main__':
    app.run()