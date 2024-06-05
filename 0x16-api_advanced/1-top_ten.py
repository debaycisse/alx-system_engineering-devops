#!/usr/bin/python3
"""This modules houses the definition of a function that prints out
the first 10 of hot posts, listed for a given subreddit"""


import requests


def top_ten(subreddit):
    """prints out the first 10 of the hot posts of a given subreddit

    Args:
        subreddit - the subreddit whose 10 host posts is printed
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
    hot_topic_url = '/r/{}/hot'.format(subreddit)
    url = base_url + hot_topic_url
    response = requests.get(url, headers=headers,
                            params={'limit': '10'},
                            allow_redirects=False)

    if (response.status_code == 200):
        counter = 0
        for data in response.json()['data']['children']:
            if (counter == 10):
                break
            print(data['data']['title'])
            counter += 1
    else:
        print(None)
