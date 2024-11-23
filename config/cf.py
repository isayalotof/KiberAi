from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
tg_token = os.getenv('TG_KEY')
hf_token = os.getenv('HF_KEY')
gl_token = os.getenv('GL_KEY')
alfa_token = os.getenv('ALFA_KEY')
fusion_token = os.getenv('FUSION_KEY')
fusion_secret = os.getenv('FUSION_SECRET')

