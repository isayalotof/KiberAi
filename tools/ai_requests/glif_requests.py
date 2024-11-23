# from http.client import responses
# import json
# import requests
#
#
# from config.cf import gl_token
#
#
# def glif_req(user_input: str) -> str:
#     response = requests.post(
#         "https://simple-api.glif.app",
#         json={"id": "cm3ghhw84005kolyqzxw324wk","inputs": [f"{user_input}, realism, full hd, with out labels"]},
#         headers={"Authorization": f"{gl_token}"},
#     )
#
#     response_dict = json.loads(response.content)
#     return response_dict['output']

