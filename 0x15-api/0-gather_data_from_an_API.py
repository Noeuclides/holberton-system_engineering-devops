#!/usr/bin/python3
"""return information about employee
"""

import requests
from sys import argv

try:
    req_user = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': argv[1]})
    req_todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                            params={'userId': argv[1]})
    info_user = req_user.json()
    name = info_user[0].get('name')
    info_todo = req_todo.json()
    done = 0
    task = len(info_todo)
    for i in range(task):
        if info_todo[i].get('completed') is True:
            done = done + 1
    print("Employee {} is done with tasks({}/{}):".format(name, done, task))
    for i in range(task):
        if info_todo[i].get('completed') is True:
            print("\t {}".format(info_todo[i].get('title')))
except:
    pass
