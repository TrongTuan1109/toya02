# Thu vien Requests
import requests
url="?platform=pc"
url_2="https://www.gamerpower.com/api/giveaways?type=game"
# response=requests.get(url)
# response_json=response.json()
# print(response_json)
# print(response.status_code)

# Thu vien urllib
import urllib.request as urllib_request
import json
# with urllib_request.urlopen(url) as response:
#     body = response.read().decode()
#     print(body)

# Thu vien HTTP
# https://www.gamerpower.com/api-reaQd
import http.client as http_client

host="www.gamerpower.com"
data = http_client.HTTPSConnection(host)
data.request("GET",f"/api/giveaways{url}",headers={"Host": host})
response=data.getresponse()
print(response.read().decode())
