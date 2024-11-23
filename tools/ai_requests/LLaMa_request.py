from huggingface_hub import InferenceClient
from config.cf import hf_token



def llama_req(user_prompt: str) -> str:



	client = InferenceClient(api_key=hf_token)

	messages = [
		{
			"role": "user",
			"content": f"""Пользователь понимает только русский язык, поэтому используй для ответа, только его,
					   но названия вещей можно писать по английски если это необходимо, так же можно писать на python,
					    C++ и JS:{user_prompt}"""
		}
	]

	completion = client.chat.completions.create(
		model="meta-llama/Llama-3.1-70B-Instruct",
		messages=messages,
		max_tokens=500
	)


	return str(completion.choices[0].message.content)



