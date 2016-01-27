from __future__ import division, print_function

import json
from time import sleep
import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
api = twitter.Twitter(auth=auth)


def retrieve_timeline(screen_name):

    print("Beginning retrieval of " + screen_name)
    try:
        timeline = api.statuses.user_timeline(screen_name=screen_name,
                                              count=200, include_rts=1)
    except:
        print("Reached rate limit; sleeping 15 minutes")
        sleep(900)
        timeline = api.statuses.user_timeline(screen_name=screen_name,
                                              count=200, include_rts=1)

    ntweets = len(timeline)
    if ntweets < 200:
        return timeline
    while ntweets == 200:
        min_id = min([tweet["id"] for tweet in timeline])
        try:
            next_timeline = api.statuses.user_timeline(screen_name=screen_name,
                                                       count=200,
                                                       max_id=min_id - 1,
                                                       include_rts=1)
        except:
            print("Reached rate limit; sleeping 15 minutes")
            sleep(900)
            next_timeline = api.statuses.user_timeline(screen_name=screen_name,
                                                       count=200,
                                                       max_id=min_id - 1,
                                                       include_rts=1)
        ntweets = len(next_timeline)
        timeline += next_timeline
    return timeline

senators = api.lists.members(
    owner_screen_name="gov", slug="us-senate", count=100)
screen_names = [d["screen_name"] for d in senators["users"]]

timelines = [retrieve_timeline(screen_name=name) for name in screen_names]
with open("timelines.json", "w") as f:
    json.dump(timelines, f, indent=4, sort_keys=True)


# Step 2: Get additional data for each senator (party, state, etc.)
# and match up with twitter data

import requests

apikey = ''
query_params = {'apikey': apikey,
                'chamber': 'senate',
                'per_page': 10,
                'page': 1}
endpoint = 'http://congress.api.sunlightfoundation.com/legislators?'
response = requests.get(endpoint, params=query_params)
sen_dict = json.loads(response.content)
sen_list = sen_dict["results"]

for p in range(2, 11):
    query_params["page"] = p
    response = requests.get(endpoint, params=query_params)
    sen_dict = json.loads(response.content)
    sen_list += sen_dict["results"]

screen_names_sunlight = [sen["twitter_id"] for sen in sen_list]
screen_names_sunlight.count(None)

# in twitter data but not sunlight data
set(screen_names).difference(set(screen_names_sunlight))
# in sunlight data but not twitter data
set(screen_names_sunlight).difference(set(screen_names))


def levenshtein(a, b):
    """ Calculates the Levenshtein distance between a and b.
    from http://hetland.org/coding/python/levenshtein.py

    For other implementations, see
    http://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance
    """
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]

realnames_twitter = [s["name"] for s in senators["users"]]
realnames_sunlight = [
    " ".join([sen["first_name"], sen["last_name"]]) for sen in sen_list]

# loop through in order of twitter data
# find the index of the closest match in the sunlight data


def findlowermatch(name, namelist):
    # returns only the first match, if there is one
    index = [i for i, t in enumerate(
        namelist) if t is not None and t.lower() == name.lower()]
    if len(index) == 0:
        return None
    return index[0]


def findlevmatch(name, namelist):
    name_dists = [levenshtein(name, nm) for nm in namelist]
    return name_dists.index(min(name_dists))

index = [findlowermatch(name, screen_names_sunlight) for name in screen_names]
for i, name in enumerate(realnames_twitter):
    if index[i] is None:
        index[i] = findlevmatch(name, realnames_sunlight)
        print("Matching " + name + " with " + realnames_sunlight[index[i]])

# fix the one mistake
index[realnames_twitter.index("FrankenCommTeam")] = realnames_sunlight.index(
    "Alan Franken")

# verify matches
for i, name in enumerate(realnames_twitter):
    print(name, "---", realnames_sunlight[index[i]])

import pandas as pd

df = pd.DataFrame([sen_list[i] for i in index])
df.to_csv('senators.csv', encoding='utf-8', index_label=False)
