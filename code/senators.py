from __future__ import division, print_function

import json

with open("senators-list.json") as f:
    senators = json.load(f)

with open("timelines.json") as f:
    timelines = json.load(f)

names = [d["screen_name"] for d in senators["users"]]

type(timelines)
len(timelines)
len(timelines[0])

# check who has the most followers
followers = [t[0]["user"]["followers_count"] for t in timelines]
zipped = zip(names, followers)
zipped.sort(key=itemgetter(1))

# get all the tweets and see what words are used
tweets = [" ".join([tweet["text"] for tweet in tweets])
                          for tweets in timelines]
words = [w for text in tweets
           for w in re.split('\W', text) if w]
vocab = sorted(set(words))

# construct term-document matrix
M = np.zeros([len(tweets), len(vocab)])
for n, tweet in enumerate(tweets):
    for m, term in enumerate(vocab):
        M[n, m] = tweet.count(term)

# pca using scikit-learn
from sklearn import decomposition
pca = decomposition.PCA(n_components=2)
pca.fit(M)
pc = pca.transform(M)
plt.scatter(pc[:, 0], pc[:, 1])
plt.show()
