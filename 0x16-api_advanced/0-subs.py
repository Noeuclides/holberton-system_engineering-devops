#!/usr/bin/python3
"""query the number of suscribers Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """get number of suscribers
    """
    try:
        url_base = 'https://www.reddit.com/' + 'r/' + subreddit + '/about.json'
        head = {"user-agent": 'N'}
        r = requests.get(url_base, headers=head, allow_redirects=False)
        if r.status_code != 200:
            return(0)
        data = r.json().get('data')
        return(data.get('subscribers'))
    except:
        pass
