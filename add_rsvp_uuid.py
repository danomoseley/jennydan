#!/usr/bin/python3.10

import configparser
import pandas
import requests
import uuid

config = configparser.RawConfigParser()
config.read('config.cfg')

cloudflare_api_token = config.get('cloudflare_d1', 'api_token')
cloudflare_account_id = config.get('cloudflare_d1', 'account_id')
cloudflare_database_id = config.get('cloudflare_d1', 'database_id')

endpoint = f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_account_id}/d1/database/{cloudflare_database_id}/query"
data = {"sql": "SELECT rowid, * FROM rsvp where uuid IS NULL;"}
headers = {"Authorization": f"Bearer {cloudflare_api_token}", "Content-Type": "application/json"}

response = requests.post(endpoint, json=data, headers=headers).json()

if response['success']:

    results = response['result'][0]['results']

    for result in results:
        rsvp_uuid = uuid.uuid4().hex
        data = {"sql": f"UPDATE rsvp set uuid = '{rsvp_uuid}' WHERE rowid = {result['rowid']};"}
        response = requests.post(endpoint, json=data, headers=headers).json()
        print(response)
else:
    print(response)
