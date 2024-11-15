import requests

from config.cf import gl_token

response = requests.post(
    "https://simple-api.glif.app",
    json={"id": "clgh1vxtu0011mo081dplq3xs", "inputs": [f"{user_input}"]},
    headers={"Authorization": f"{gl_token}"},
)
print(response.content)