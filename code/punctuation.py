from __future__ import division, print_function

import re
import string


RE_PUNCTUATION = re.compile(r'[^!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]')


def all_punct1(tweet):
    r"""Check if tweet is just punctuation marks.

    Parameters
    ----------
    tweet : str

    Returns
    -------
    bool
        True if all characters in tweet are punctuation.

    Examples
    --------
    >>> all_punct1("cat")
    False
    >>> all_punct1("cat.")
    False
    >>> all_punct1(".")
    True
    >>> all_punct1("12")
    False
    >>> all_punct1(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct1("")
    True
    """
    return all([c in string.punctuation for c in tweet])


def all_punct2(tweet):
    return set(tweet).issubset(set(string.punctuation))


def all_punct3(tweet):
    return set(tweet).issubset(string.punctuation)


def all_punct22(tweet, vocab=set(string.punctuation)):
    return set(tweet).issubset(vocab)


def all_punct4(tweet):
    """


    all_punct4("")
    all_punct4("cat")
    all_punct4("c!")
    all_punct4("#$")
    all_punct4("#$************************!!")
    all_punct5(r'[^!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]')
    all_punct5(r'^!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~')
    """
    search = re.compile(r'[^!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]').search
    return not bool(search(tweet))


def all_punct5(tweet, search=RE_PUNCTUATION.search):
    """
    all_punct4("")
    all_punct4("cat")
    all_punct4("c!")
    all_punct4("#$")
    """
    return not bool(search(tweet))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
