from googletrans import Translator, constants
from pprint import pprint


translator = Translator()

translation = translator.translate(f"привет мир", src="ru", dest='en')
translated_user_promt = translation.text

print(translated_user_promt)