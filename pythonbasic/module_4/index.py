import json
from os import system
import pprint

from dataset import users, countries

users_wrong_password = []
girls_drivers = []
best_occupation = {
    'occupation': '',
    'salary': 0
}
max_salary = 0
fef = {}
remove = []
for index, user in enumerate(users):
    if user['password'].isdigit():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})
    if user.get('friends'):
        for friend in user.get('friends'):
            if friend.get('cars') and friend.get('sex') == 'F':
                girls_drivers.append(friend.get('name'))
            if friend.get('job'):
                if friend['job']['salary'] > max_salary:
                    best_occupation['occupation'] = friend['job']['occupation']
                    best_occupation['salary'] = friend['job']['salary']
            if friend.get('cars'):
                if friend.get('flights'):
                    avg_flights = round(len(friend['cars']) / len(friend['flights']), 5)
            if friend.get('flights'):
                for flight in friend['flights']:
                    if flight['country'] in countries:
                        pass
                        # try:
                        #     users.remove(users[index])
                        # except:
                        #     continue
print(users_wrong_password)