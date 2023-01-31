import requests
import datetime
import os


NUTRITION_Apikey = os.environ["Api_key"]
NUTRITION_ID = os.environ['ID']
NUTRITION_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 170
AGE = 30
TOKEN = os.environ["TOKEN"]

HEADERS = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_Apikey,
}
exercise_params = {
    "query": input("what did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=NUTRITION_Endpoint, json=exercise_params, headers=HEADERS)
exercise_data = response.json()
print(exercise_data)

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

sheety_endpoint = os.environ["sheety_endpoint"]
sheet_input = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise_data["exercises"][0]['user_input'],
        "duration": exercise_data["exercises"][0]['duration_min'],
        "calories": exercise_data["exercises"][0]['nf_calories']
    }
}
header = {
    "Authorization": TOKEN
}

response_sheety = requests.post(url=sheety_endpoint, json=sheet_input, headers=header)
print(response_sheety.text)
