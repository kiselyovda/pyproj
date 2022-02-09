from pprint import pprint

import requests


response = requests.request('GET', 'https://api.github.com/users/pumpskill/repos')
repos_list = response.json()
for repo in repos_list:
    print(repo['full_name'])
