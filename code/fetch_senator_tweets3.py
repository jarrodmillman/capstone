from __future__ import division, print_function

import json
from time import sleep

import numpy as np
import pandas as pd
import twitter


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
api = twitter.Twitter(auth=auth)


def retrieve_followers(screen_name):

    print("Beginning retrieval of " + screen_name)
    ids = []
    cursor = -1

    while cursor != 0:

        try:
            followers = api.followers.ids(
                screen_name=screen_name, cursor=cursor)
        except:
            print("Reached rate limit; sleeping 15 minutes")
            sleep(900)
            followers = api.followers.ids(
                screen_name=screen_name, cursor=cursor)

        cursor = followers["next_cursor"]
        ids += followers["ids"]

    return ids


with open("senators-list.json") as f:
    senators = json.load(f)

screen_names = [d["screen_name"] for d in senators["users"]]
followers = [retrieve_followers(screen_name=name) for name in screen_names]

with open("followers.json", "w") as f:
    json.dump(followers, f, indent=4, sort_keys=True)

ids = [s["id"] for s in senators["users"]]
M = np.asmatrix(np.zeros([100, 100]))
for i, fol in enumerate(followers):
    print(i)
    for j, idj in enumerate(ids):
        if idj in fol:
            M[i, j] = 1

M_df = pd.DataFrame(M)
M_df.to_csv("followersmatrix.csv", encoding="utf-8", index_label=False)
