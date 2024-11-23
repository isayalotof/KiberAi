import json
import time
import base64
import requests
from PIL import Image
from io import BytesIO
from config.cf import fusion_token, fusion_secret



class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)

    def decode_image(self, img_base64):
        img_data = base64.b64decode(img_base64)
        img = Image.open(BytesIO(img_data)).convert('RGB')
        return img

def get_photo(prompt: str, user_id: str):
    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', fusion_token, fusion_secret)
    uuid = api.generate(prompt, api.get_model())
    images = api.check_generation(uuid)
    if not images:
        raise ValueError("Изображения не были сгенерированы.")
    dec_img = api.decode_image(images[0])
    dec_img.save(f'tools/ai_requests/img/img_{user_id}.png')
    return f'tools/ai_requests/img/img_{user_id}.png'

# from huggingface_hub import InferenceClient
#
# from config.cf import hf_token
#
#
# client = InferenceClient("strangerzonehf/Flux-Super-Realism-LoRA", token=hf_token)
#
# def get_photo(prompt: str, user_id: str):
#     image = client.text_to_image(prompt)
#     image.save(f'tools/ai_requests/img/img_{user_id}.png')
#     return f'tools/ai_requests/img/img_{user_id}.png'