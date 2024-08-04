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
data = {"sql": "select meal_choice.meal_description as 'Meal Choice', count(*) as 'Total Count' from rsvp_guest JOIN meal_choice ON rsvp_guest.meal_choice_rowid = meal_choice.rowid group by rsvp_guest.meal_choice_rowid;"}
headers = {"Authorization": f"Bearer {cloudflare_api_token}", "Content-Type": "application/json"}

response = requests.post(endpoint, json=data, headers=headers).json()

if response['success']:
    results = response['result'][0]['results']
    print(f"{len(results)} results written to meal_totals.xlsx")
    pandas.json_normalize(results).to_excel('meal_totals.xlsx')
else:
    print(response)
