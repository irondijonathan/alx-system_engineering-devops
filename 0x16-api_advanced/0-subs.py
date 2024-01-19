#!/usr/bin/python3
"""This Defines a function for getting
number of subreddit subscribers"""


def number_of_subscribers(subreddit):
    """
    This Gets the number of subscribers to
    a subreddit.

    Args:
        subreddit (str): the name of the subreddit

    Returns:
        This returns the number of subs else 0 for invalid name.
    """
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(
        url, headers={"User-Agent": "My-User-Agent"}, allow_redirects=False
    )
    if response.status_code >= 300:
        return 0
    else:
        data = response.json()
        return data["data"]["subscribers"]
