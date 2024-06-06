#!/usr/bin/python3
"""This houses the definition of a function that recusrively calls
reddit api and returns a list containing the titles of all hot
articles for a given subreddit."""


import requests


def recurse(subreddit, hot_list=[], url=None):
    """calls reddit api recursively and returns a list, containing the title
    of all the hot articles for a given subreddit

    Args:
        subreddit - the subreddit whose list of hot article
        titles are returned
        hot_list - takes the list that must be updated in each recusive call
    """
    headers = {'User-Agent': 'ALXAdvanceAPI/0.0.2'}
    client_id = 'u-gOcsSz4rOBcxpFTj5iKQ'
    secret_key = '0N5ptIar_TTcKr5b5pgEuf2oqYeswg'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    data = {'grant_type': 'password', 'username': 'debaycisse',
            'password': 'TechThing@24'}

    # getting and setting the token
    TOKEN = requests.post('https://www.reddit.com/api/v1/access_token',
                          auth=auth, data=data, headers=headers).json()
    TOKEN = TOKEN['access_token']
    headers['Authorization'] = 'bearer {}'.format(TOKEN)

    # calling the reddit api
    base_url = 'https://oauth.reddit.com'
    subreddit_url = '/r/{}/hot'.format(subreddit)
    main_url = base_url + subreddit_url

    # making the call
    if (not url):
        response = requests.get(main_url, headers=headers,
                                allow_redirects=False)
    else:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)

    if (response.status_code == 200):
        after_val = response.json()['data']['after']
        if (len(hot_list) < 1):
            for obj in response.json()['data']['children']:
                hot_list.append(obj['data']['title'])
            if (after_val):
                new_url = main_url + '?after={}'.format(after_val)
                return recurse(subreddit, hot_list, new_url)
            else:
                return hot_list
        else:
            for obj in response.json()['data']['children']:
                hot_list.append(obj['data']['title'])
            if (not after_val):
                return (hot_list)
            else:
                new_url = main_url + '?after={}'.format(after_val)
                return recurse(subreddit, hot_list, new_url)
    else:
        return None
