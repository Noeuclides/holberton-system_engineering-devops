#!/usr/bin/python3
"""return information about employee
"""
import csv
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
    row = []
    filename = argv[1] + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for i in range(task):
            writer.writerow([argv[1], username, info_todo[i].get(
                'completed'), info_todo[i].get('title')])
except BaseException:
    pass
