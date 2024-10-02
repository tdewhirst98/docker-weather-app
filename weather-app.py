from dotenv import load_dotenv
import os
import requests
import json

json_file = './response.json'

load_dotenv()

api_key = os.getenv("API_KEY")

lat = '44.637489'
long = '76.326607'

if not api_key:
    raise ValueError("API KEY is missing in environment variable")


api_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}9&appid={api_key}"


response = requests.get(api_call)

with open(json_file, 'w') as f:
    json.dump(response.json(),f, indent=4)

with open(json_file, 'r') as f:
    data = json.load(f)

print( f"Looks like today in {data['name']} {data['sys']['country']} the weather is {data['weather'][0]['description']}")