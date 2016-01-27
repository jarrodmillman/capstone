from __future__ import division, print_function

import json
from operator import itemgetter
import string

from gensim import corpora, models
import nltk
from nltk import word_tokenize, FreqDist
import pandas as pd


# Step 1: Load data

with open("timelines.json") as f:
    timelines = json.load(f)

df = pd.read_csv("senators.csv")


# Step 2: Create some additional datastructures

tweet_list = [[tweet["text"] for tweet in tl] for tl in timelines]
text_list = [" ".join(tl) for tl in tweet_list]  # tweets back to back

text_repub = " ".join(
    [text for i, text in enumerate(text_list) if df["party"][i] == "R"])
text_dem = " ".join(
    [text for i, text in enumerate(text_list) if df["party"][i] == "D"])


# Step 3: Preliminary text analysis using nltk

textnltk_repub = nltk.Text(word_tokenize(text_repub))
textnltk_dem = nltk.Text(word_tokenize(text_dem))

textnltk_repub.collocations()
textnltk_dem.collocations()

textnltk_repub.count("climate") / len(textnltk_repub)
textnltk_dem.count("climate") / len(textnltk_dem)

textnltk_repub.count("Obama") / len(textnltk_repub)
textnltk_dem.count("Obama") / len(textnltk_dem)

textnltk_repub.concordance("Obama")
textnltk_dem.concordance("Obama")


# Step 4: Clean up tokens

stopwords = nltk.corpus.stopwords.words("english")


def tweet_clean(t):
    cleaned_words = [word for word in t.split()
                     if "http" not in word
                     and not word.startswith("@")
                     and not word.startswith(".@")
                     and not word.startswith("#")
                     and word != "RT"]
    return " ".join(cleaned_words)


def all_punct(x):
    return all([char in string.punctuation for char in x])


def my_tokenize(text):
    init_words = word_tokenize(text)
    return [w.lower() for w in init_words if
            not all_punct(w) and w.lower() not in stopwords]


tweet_list_cleaned = [[my_tokenize(tweet_clean(tweet)) for tweet in tweets]
                      for tweets in tweet_list]
tokens_list_cleaned = [sum(tweets, []) for tweets in tweet_list_cleaned]


# Step 5: Look for words more frequently used by dems or repubs

tokens_repub = sum([tokens for i, tokens in enumerate(tokens_list_cleaned)
                    if df["party"][i] == "R"], [])
tokens_dem = sum([tokens for i, tokens in enumerate(tokens_list_cleaned)
                  if df["party"][i] == "D"], [])

words = set(tokens_repub + tokens_dem)

fd_repub = FreqDist(nltk.Text(tokens_repub))
fd_dem = FreqDist(nltk.Text(tokens_dem))

# find frequently occuring words, filter out the short ones (use state
# abbreviations)
highfreq_words = [word for word in list(words)
                  if fd_repub[word] + fd_dem[word] > 20 and len(word) > 2]

hf_repub = [(word, fd_repub[word], fd_dem[word]) for word in highfreq_words if
            fd_repub[word] / len(tokens_repub) > 5.0 * fd_dem[word] / len(tokens_dem)]
hf_dem = [(word, fd_dem[word], fd_repub[word]) for word in highfreq_words if
          fd_dem[word] / len(tokens_dem) > 5.0 * fd_repub[word] / len(tokens_repub)]

sorted(hf_repub, key=itemgetter(1), reverse=True)
sorted(hf_dem, key=itemgetter(1), reverse=True)

textnltk_repub.concordance("obamacare")
textnltk_dem.concordance("obamacare")


# Step 6: Use gensim to create a bag-of-words representation for each senator
# and project it into a 2-dimensional subspace for visualization using LSI
# For more details see:
# http://radimrehurek.com/gensim/tutorial.html
# https://en.wikipedia.org/wiki/Latent_semantic_indexing
# https://en.wikipedia.org/wiki/Tf-idf


# limit analysis to high-frequency words only
dictionary = corpora.Dictionary([highfreq_words])
corpus = [dictionary.doc2bow(tokens) for tokens in tokens_list_cleaned]
tfidf = models.TfidfModel(corpus, normalize=True)
corpus_tfidf = tfidf[corpus]

#tfidf_df = pd.DataFrame([[v[1] for v in vector] for vector in corpus_tfidf])
#tfidf_df.to_csv('tfidf.csv', encoding='utf-8', index_label=False)

num_topics = 10
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=num_topics)

lsi.print_topics(num_topics)

lsi_df = pd.DataFrame([[v[1] for v in vector] for vector in lsi[corpus]])
lsi_df.to_csv('lsi.csv', encoding='utf-8', index_label=False)
