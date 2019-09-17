#!/usr/bin/python3
"""export to json
"""
import csv
import json
import requests


try:
    req_user = requests.get('https://jsonplaceholder.typicode.com/users')
    req_todo = requests.get('https://jsonplaceholder.typicode.com/todos')

    info_user = req_user.json()
    name = info_user[0].get('name')
    username = info_user[0].get('username')
    id = info_user[0].get('id')
    info_todo = req_todo.json()
    task = len(info_todo)
    info_d = {}
    filename = "todo_all_employees.json"

    for i in range(len(info_user)):
        info_l = []
        user = info_user[i]
        for j in range(len(info_todo)):
            todo = info_todo[j]
            if user.get('id') == todo.get('userId'):
                info_l.append({'task': todo.get('title'),
                               "completed": todo.get('completed'),
                               "username": user.get('username')})
        info_d[user.get('id')] = info_l
    with open(filename, mode='w') as f:
        json.dump(info_d, f)
except:
    pass
