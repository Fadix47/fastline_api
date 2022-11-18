import requests

token = "TOKEN"
guild_id = "GUILD_ID"
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

resp = requests.request("GET", f'https://fastline.space/api/{guild_id}', headers=headers, data={"token": token})

print(resp.text)
