from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
tg_token = os.getenv('TG_KEY')
hf_token = os.getenv('HF_KEY')
gl_token = os.getenv('GL_KEY')