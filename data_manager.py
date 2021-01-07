from pprint import pprint
import config
import requests

SHEETY_PRICES_ENDPOINT = config.SHEETY_PRICES_ENDPOINT
SHEETY_USERS_ENDPOINT = config.SHEETY_USERS_ENDPOINT

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def add_user(self, user_body):
        requests.post(url=SHEETY_USERS_ENDPOINT, json=user_body)


    def get_users(self):
        res = requests.get(url=SHEETY_USERS_ENDPOINT)
        user_list = res.json()["users"]
        return user_list

