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
data = {"sql": "SELECT rowid, * FROM rsvp where attending;"}
headers = {"Authorization": f"Bearer {cloudflare_api_token}", "Content-Type": "application/json"}

response = requests.post(endpoint, json=data, headers=headers).json()

#data = {"sql": f"create table rsvp_guest(rsvp_rowid INTEGER NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, meal_choice_rowid INTEGER);"}
#response = requests.post(endpoint, json=data, headers=headers).json()

if response['success']:

    results = response['result'][0]['results']

    for result in results:
        data = {"sql": f"INSERT INTO rsvp_guest (rsvp_rowid, first_name, last_name) values ({result['rowid']}, '{result['first_name']}', '{result['last_name']}');"}
        response = requests.post(endpoint, json=data, headers=headers).json()
        print(response)
        if result['guest_names']:
            guests = result['guest_names'].splitlines()
            for guest in guests:
                guest_name_parts = guest.split()
                if len(guest_name_parts) == 2:
                    guest_first_name = guest_name_parts[0]
                    guest_last_name = guest_name_parts[1]
                elif len(guest_name_parts) == 3:
                    guest_first_name = f"{guest_name_parts[0]} {guest_name_parts[1]}"
                    guest_last_name = guest_name_parts[2]
                else:
                    guest_first_name = guest
                    guest_last_name = ""
                data = {"sql": f"INSERT INTO rsvp_guest (rsvp_rowid, first_name, last_name) values ({result['rowid']}, '{guest_first_name}', '{guest_last_name}');"}
                response = requests.post(endpoint, json=data, headers=headers).json()
                print(response)
else:
    print(response)
