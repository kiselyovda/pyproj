import json
from os import system
import pprint

from dataset import users, countries

users_wrong_password = []
girls_drivers = []
best_occupation = {}
max_salary = 0
max_friends_total_salary = 0
vip_user = ''
for index, user in enumerate(users):
    if user['password'].isdigit():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})
    if user.get('friends'):
        friends_total_salary = 0
        for friend in user.get('friends'):
            if friend.get('cars') and friend.get('sex') == 'F':
                girls_drivers.append(friend.get('name'))
            if friend.get('job'):
                friends_total_salary += friend['job']['salary']
                if friends_total_salary > max_friends_total_salary:
                    max_friends_total_salary = friends_total_salary
                    vip_user = user['name']
                if friend['job']['salary'] > max_salary:
                    max_salary = friend['job']['salary']
                    best_occupation['occupation'] = friend['job']['occupation']
                    best_occupation['salary'] = friend['job']['salary']

avg_flights = 0
friends_with_cars = 0
total_flights = 0
for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        cars = friend.get('cars', None)
        if cars:
            friends_with_cars += 1
            total_flights += len(friend.get('flights', []))
avg_flights = round(total_flights / friends_with_cars, 5) if friends_with_cars else 0

i = 0
while i < len(users):
    need_remove = False
    friends = users[i].get('friends', [])
    for friend in friends:
        flights = friend.get('flights', [])
        for flight in flights:
            if flight['country'] in countries:
                need_remove = True
                break
        if need_remove:
            break

    if need_remove:
        del users[i]
    else:
        i += 1