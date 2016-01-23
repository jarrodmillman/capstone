from __future__ import division, print_function

import json
from operator import itemgetter
import re


# 1. Load senators-list.json as senators.
with open("senators-list.json") as f:
    senators = json.load(f)

# 2. Load timelines.json as timelines.
with open("timelines.json") as f:
    timelines = json.load(f)


# 3. What type of datastructure is timelines?
type(timelines)

# 4. How many timelines are there? What does each timeline correspond to?
len(timelines)
len(timelines[0])
len(timelines[1])
timelines[0]
timelines[0][0]
timelines[0][0].keys()

timelines[0][0]["truncated"]
timelines[0][0]["text"]
timelines[0][0]["favorite_count"]
timelines[0][0]["user"].keys()
timelines[0][0]["user"]["favourites_count"]
timelines[0][0]["user"]["followers_count"]
timelines[0][0]["user"]["friends_count"]
timelines[0][0]["user"]["description"]

# 5. Make a list of each senator’s screen name using the variable senators.
names = [d["screen_name"] for d in senators["users"]]

# 6. Make a list of the number of followers each senator has.

# 6.1. take the 'followers_count' for the first tweet for each senator
[x["user"]["followers_count"] for x in timelines[0]]
followers = [t[0]["user"]["followers_count"] for t in timelines]

# 6.2. connect the names with their follower counts and sort on the counts
followers = zip(names, followers)
followers.sort(key=itemgetter(1))

# 7. What is the screen name of the senator with the largest number of
# followers?
followers[0]
followers[-1]

# who is the most favorited

favorite = [t[0]["user"]["favourites_count"] for t in timelines]
favorite = zip(names, favorite)
favorite.sort(key=itemgetter(1))
favorite[0]
favorite[-1]

# 8. Make a list called tweets such that each element of the list contains
# all of one senator’s tweets concatenated as one string.

# let's start looking at the text in a tweet
tweet = timelines[0][0]["text"]
tweet

# how might we split it up?
tweet.split()
re.split('\W', tweet)

# get all the tweets and see what words are used
tweets = [" ".join([tweet["text"] for tweet in tweets])
          for tweets in timelines]
words = [w for text in tweets
         for w in re.split('\W', text) if w]

# 9. Create a sorted list of all the unique words used in any senators
# tweets and call it vocab.
vocab = sorted(set(words))

# find frequently occuring words, filter out the short ones

frequent_words = [w for w in vocab if len(w) > 4 and words.count(w) > 30]
