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

# could check who has the most followers
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



# Step 2: Get additional data for each senator (party, state, etc.)
# and match up with twitter data

# Step 3: Preliminary text analysis using nltk

tweet_list = [[tweet["text"] for tweet in tl] for tl in timelines]
text_list = [' '.join(tl) for tl in tweet_list]  # tweets back to back

import string
stopwords = nltk.corpus.stopwords.words('english')


def tweet_clean(t):
    cleaned_words = [word for word in t.split()
                     if 'http' not in word
                     and not word.startswith('@')
                     and not word.startswith('.@')
                     and not word.startswith('#')
                     and word != 'RT']
    return(' '.join(cleaned_words))


def all_punct(x):
    return(all([char in string.punctuation for char in x]))


def my_tokenize(text):
    init_words = word_tokenize(text)
    return([w.lower() for w in init_words if not all_punct(w) and w.lower() not in stopwords])

tweet_list_cleaned = [
    [my_tokenize(tweet_clean(tweet)) for tweet in tweets] for tweets in tweet_list]
tokens_list_cleaned = [sum(tweets, []) for tweets in tweet_list_cleaned]


words = set(tokens_repub + tokens_dem)

# find frequently occuring words, filter out the short ones (use state
# abbreviations)
highfreq_words = [word for word in list(words)
                  if fd_repub[word]+fd_dem[word] > 20 and len(word) > 2]
