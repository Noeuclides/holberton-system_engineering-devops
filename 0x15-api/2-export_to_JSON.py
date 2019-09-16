#!/usr/bin/python3
"""export to json
"""
import csv
import json
import requests
from sys import argv

try:
    req_user = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': argv[1]})
    req_todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': argv[1]})
    info_user = req_user.json()
    name = info_user[0].get('name')
    username = info_user[0].get('username')
    id = info_user[0].get('id')
    info_todo = req_todo.json()
    task = len(info_todo)
    info_l = []
    info_d = {}
    filename = argv[1] + '.json'

    for i in range(task):
        info_l.append({'task': info_todo[i].get('title'),
                       "completed": info_todo[i].get('completed'),
                       "username": username})
        info_d[id] = info_l
        with open(filename, mode='w') as f:
            json.dump(info_d, f)
except BaseException:
    pass
