import requests
from dotenv import load_dotenv

# load_dotenv

url = 'https://randomuser.me/api'
result = {}
try:
    responds =  requests.get(url)
    result = responds.json()
except Exception as e:
    print('Bad Request! check url')
  
if(result != {}):
    age = result["results"][0]['dob']['age']
    name = result["results"][0]['name']["first"]
    # print(age)
    if(age >= 18):
        print('Hello '+name+ ' You can drive')    
    else:
        print('Hello ' +name+'!')

    