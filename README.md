# FAQ

### Q: Which methods are supported in your API?
### A:You can use only method "GET" in our API, so we provide read-only information.

### Q: Who can get access to this information?
### A: We are using token-system, so everyone, who have token can have access to this information.

### Q: Which information can I get on the API?
### A: You can view only inforamtion about members on server, which token contains. You can see only EXP, online, balance and history of punishments (`max: 50`). You view same information on your guild by using commands, which accessable to everyone by default.

### Q: Where can I get token to use API?
### A: Create ticket on https://fastline.space/discord in tickets channel. After admins confirm that you are OWNER of this server you will get the token.

# Short example on python code

```py
import requests

token = 'HERE_IS_YOUR_TOKEN'
guild_id = '100000000000000000'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

resp = requests.request("GET", f'https://reina.guru/api/{guild_id}', headers=headers, data={"token": token})

print(resp.text) # returns json with information from your server

```

### Response example

```json

{
  "418380853379596288":
    {
      "balance":0,
      "exp":0,
      "online":0,
      "punishlist":[]
    },
  "538253712829710336":
    {
      "balance":0,
      "exp":0,
      "online":0,
      "punishlist":[]
    }
}

```
