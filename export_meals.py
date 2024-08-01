#!/usr/bin/python3.10

import configparser
import pandas
import requests

config = configparser.RawConfigParser()
config.read('config.cfg')

cloudflare_api_token = config.get('cloudflare_d1', 'api_token')
cloudflare_account_id = config.get('cloudflare_d1', 'account_id')
cloudflare_database_id = config.get('cloudflare_d1', 'database_id')

endpoint = f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_account_id}/d1/database/{cloudflare_database_id}/query"
data = {"sql": "select rsvp_guest.first_name, rsvp_guest.last_name, meal_choice.meal_description from rsvp_guest JOIN meal_choice on rsvp_guest.meal_choice_rowid = meal_choice.rowid WHERE rsvp_guest.meal_choice_rowid is not NULL and rsvp_guest.meal_choice_rowid not in (5,6) ORDER BY rsvp_guest.last_name, rsvp_guest.first_name;"}
headers = {"Authorization": f"Bearer {cloudflare_api_token}", "Content-Type": "application/json"}

response = requests.post(endpoint, json=data, headers=headers).json()

if response['success']:
    results = response['result'][0]['results']
    print(f"{len(results)} results written to meals.xlsx")
    pandas.json_normalize(results).to_excel('meals.xlsx')
else:
    print(response)
