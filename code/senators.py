from __future__ import division, print_function

import csv
import json
from operator import itemgetter
import re
import string

import numpy as np


with open("senators-list.json") as f:
    senators = json.load(f)

with open("timelines.json") as f:
    timelines = json.load(f)

names = [d["screen_name"] for d in senators["users"]]

type(timelines)
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

# who has the most followers

# 1. take the 'followers_count' for the first tweet for each senator
[x["user"]["followers_count"] for x in timelines[0]]
followers = [t[0]["user"]["followers_count"] for t in timelines]

# 2. connect the names with their follower counts and sort on the counts
followers = zip(names, followers)
followers.sort(key=itemgetter(1))
followers[0]
followers[-1]

# who is the most favorited

favorite = [t[0]["user"]["favourites_count"] for t in timelines]
favorite = zip(names, favorite)
favorite.sort(key=itemgetter(1))
favorite[0]
favorite[-1]

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
vocab = sorted(set(words))

# find frequently occuring words, filter out the short ones
frequent_words = [w for w in vocab if len(w) > 4 and words.count(w) > 30]


# construct term-document matrix
M = np.zeros([len(tweets), len(vocab)])
for n, tweet in enumerate(tweets):
    for m, term in enumerate(vocab):
        M[n, m] = tweet.count(term)


# Step 2: Get additional data for each senator (party, state, etc.)
# and match up with twitter data

# Step 3: Preliminary text analysis using nltk

tweets_list = [[tweet["text"] for tweet in tl] for tl in timelines]

# http://www.textfixer.com/resources/common-english-words.txt
with open("common-english-words.txt") as f:
    stopwords = csv.reader(f).next()


# def clean(tweet):
#    cleaned_words = [word.lower() for word in tweet.split()
#                     if 'http' not in word
#                     and word.isalpha()
#                     and word != 'RT']
#    return ' '.join(cleaned_words)
#
#
# def clean(tweet):
#    tweet = tweet.encode('ascii', 'ignore')
#    cleaned_words = [word.lower() for word in tweet.split()
#                     if 'http' not in word
#                     and not word.startswith('@')
#                     and not word.startswith('.@')
#                     and not word.startswith('#')
#                     and word != 'RT']
#    exclude = set(string.punctuation)
#    return ' '.join(c for c in cleaned_words if c not in exclude)


def clean(tweet):
    tweet = tweet.encode('ascii', 'ignore')
    cleaned_words = [word.lower() for word in tweet.split()
                     if 'http' not in word
                     and not word.startswith('@')
                     and not word.startswith('.@')
                     and not word.startswith('#')
                     and word != 'RT']
    return ' '.join(cleaned_words)


def all_punct(tweet):
    # all([c in string.punctuation for c in tweet])
    return set(tweet).issubset(set(string.punctuation))


def remove_punct(word):
    exclude = set(string.punctuation)
    return ''.join(c for c in word if c not in exclude)


def tokenize(tweet):
    words = [remove_punct(w) for w in clean(tweet).split()
             if not all_punct(w) and w not in stopwords]
    return ' '.join(words)


tweets_list = [[tokenize(tweet) for tweet in tweets] for tweets in tweets_list]
tokens_list = [' '.join(tweets) for tweets in tweets_list]

words = ' '.join(tokens_list).split()
vocab = sorted(set(words))
