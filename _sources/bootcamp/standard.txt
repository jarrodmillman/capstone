#######################
Standard track bootcamp
#######################

We will start by quickly working through most of the

- :ref:`python-intro`.

Then we will revisit the

- :ref:`senate-exercise`.

First we will examine the download script::

  $ wget http://jarrodmillman.com/capstone/code/fetch_senator_tweets.py

Then we will review exercise solutions::

  $ wget http://jarrodmillman.com/capstone/code/senators.py

We will conclude by tokenizing the tweets.

#. Make a list of lists where the outer list represents senators and the
   inner list contains each senator's tweets, call it ``tweets_list``

#. Write a function that takes tweet and returns a cleaned up version
   of the tweet.  Here is some example code to get you started::

       >>> def clean(tweet):
       ...     cleaned_words = [word.lower() for word in tweet.split() if
       ...                      'http' not in word and
       ...                      word.isalpha() and
       ...                      word != 'RT']
       ...     return ' '.join(cleaned_words)
       ...

#. Write a function, called ``all_punct``, which takes a word and returns
   a bool indicating whether all the characters are punctuation marks.

#.
