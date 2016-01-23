from __future__ import division, print_function

import csv
import json
from operator import itemgetter
import re
import string


with open("senators-list.json") as f:
    senators = json.load(f)

with open("timelines.json") as f:
    timelines = json.load(f)


# first get a list of lists
tweets_list = [[tweet["text"] for tweet in tl] for tl in timelines]

# def clean(tweet):
#    cleaned_words = [word.lower() for word in tweet.split() if
#                     'http' not in word and
#                     word.isalpha() and
#                     word != 'RT']
#    return ' '.join(cleaned_words)


def clean(tweet):
    tweet = tweet.encode('ascii', 'ignore')
    cleaned_words = [word.lower() for word in tweet.split() if
                     'http' not in word and
                     not word.startswith('@') and
                     not word.startswith('.@') and
                     not word.startswith('#') and
                     word != 'RT']
    return ' '.join(cleaned_words)


def all_punct(tweet):
    # all([c in string.punctuation for c in tweet])
    return set(tweet).issubset(set(string.punctuation))


def remove_punct(word):
    exclude = set(string.punctuation)
    return ''.join(c for c in word if c not in exclude)


# http://www.textfixer.com/resources/common-english-words.txt
with open("common-english-words.txt") as f:
    stopwords = csv.reader(f).next()


def tokenize(tweet):
    words = [remove_punct(w) for w in clean(tweet).split() if
             not all_punct(w) and w not in stopwords]
    return ' '.join(words)


tweets_list = [[tokenize(tweet) for tweet in tweets] for tweets in tweets_list]
tokens_list = [' '.join(tweets) for tweets in tweets_list]

words = ' '.join(tokens_list).split()
vocab = sorted(set(words))

frequent_words = [w for w in vocab if len(w) > 4 and words.count(w) > 30]

