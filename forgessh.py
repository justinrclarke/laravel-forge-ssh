import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://forge.laravel.com/api/v1/servers'
headers = {'Authorization': f'Bearer {os.environ["TOKEN"]}'}

response = requests.get(url, headers=headers)

data = response.json()

addresses = []

for index, server in enumerate(data['servers']):
    addresses.insert(index, server['ip_address'])
    print(f"{index}: {server['name']} | {server['provider']}")

server_index = input('Select a server: \n')
os.system(f'ssh -t -t forge@{addresses[int(server_index)]}')