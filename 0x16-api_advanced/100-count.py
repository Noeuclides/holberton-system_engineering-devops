#!/usr/bin/python3
"""queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """return list of all articles
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
