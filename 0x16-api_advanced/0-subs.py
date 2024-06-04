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
    base_url = 'https://www.reddit.com'
    subreddit_api_url = '/r/none_subreddit/about'
    if (subreddit):
        subreddit_api_url = '/r/{}/about'.format(subreddit)
    print(subreddit_api_url)
    url = base_url + subreddit_api_url
    print(url)
    response = requests.get(url, allow_redirects=False)
    print(response.status_code)

    if(response.status_code == 200):
        subscr_ind = response.text.index('subscribers')
        subscr = response.text[subscr_ind:subscr_ind+50]
        subscr = subscr.split('\n')[0].split('=')
        return int(eval(subscr[1]))
    else:
        return 0
