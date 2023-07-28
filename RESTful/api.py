import requests

url = 'https://randomuser.me/api'

responds =  requests.get(url)
if(responds.status_code):
    result = responds.json()
gender = result["results"][0]['gender']
print(gender)
    