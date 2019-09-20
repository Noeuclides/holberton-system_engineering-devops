#!/usr/bin/python3
"""query Reddit API and print tittles of first ten listed
"""
import requests


def top_ten(subreddit):
    """print top ten listed
    """
    url_base = 'https://www.reddit.com/' + 'r/' + subreddit + '/hot.json'
    head = {"user-agent": 'N'}
    r = requests.get(url_base, headers=head, allow_redirects=False)
    if r.status_code != 200:
        print(None)
    else:
        data = r.json().get('data')
        child = data.get('children')
        for i in range(10):
            print(child[i].get('data').get('title'))
