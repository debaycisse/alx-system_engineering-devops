#!/usr/bin/python3
"""This modules houses the function that queries reddit API to obtain the
total number of subscribers of a given subreddit. The subreddit's name is
passed from the commandline, this application is a commandline application.
"""
import requests


def number_of_subscribers(subreddit):
    """queries the subreddit api to obtain the total number
    of subscriber of the passed subreddit

    Args:
        subreddit - the passed subreddit whose subscribers are obtained
    """
    base_url = 'https://oauth.reddit.com'
    subreddit_api_url = '/r/none_subreddit/about'
    if (subreddit):
        subreddit_api_url = '/r/{}/about'.format(subreddit)
    url = base_url + subreddit_api_url
    client_id = 'u-gOcsSz4rOBcxpFTj5iKQ'
    secret_key = '0N5ptIar_TTcKr5b5pgEuf2oqYeswg'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    data = {'grant_type': 'password',
            'username': 'debaycisse', 'password': 'TechThing@24'}
    headers = {'User-Agent': 'ALXAdvanceAPI/0.0.1'}
    # obtains the access token
    TOKEN = requests.post('https://www.reddit.com/api/v1/access_token',
                          auth=auth, data=data, headers=headers).json()
    TOKEN = TOKEN['access_token']
    # set the Authorization header
    headers['Authorization'] = 'bearer {}'.format(TOKEN)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if(response.status_code == 200):
        subscribers = response.json()['data']['subscribers']
        return int(subscribers)
    else:
        return 0
