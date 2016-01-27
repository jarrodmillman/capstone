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
    >>> all_punct2("cat")
    False
    >>> all_punct2("cat.")
    False
    >>> all_punct2(".")
    True
    >>> all_punct2("12")
    False
    >>> all_punct2(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct2("")
    True
    """
    return set(tweet).issubset(set(string.punctuation))


def all_punct3(tweet):
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
    >>> all_punct3("cat")
    False
    >>> all_punct3("cat.")
    False
    >>> all_punct3(".")
    True
    >>> all_punct3("12")
    False
    >>> all_punct3(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct3("")
    True
    """
    return set(tweet).issubset(string.punctuation)


def all_punct4(tweet, vocab=set(string.punctuation)):
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
    >>> all_punct4("cat")
    False
    >>> all_punct4("cat.")
    False
    >>> all_punct4(".")
    True
    >>> all_punct4("12")
    False
    >>> all_punct4(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct4("")
    True
    """
    return set(tweet).issubset(vocab)


def all_punct5(tweet):
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
    >>> all_punct5("cat")
    False
    >>> all_punct5("cat.")
    False
    >>> all_punct5(".")
    True
    >>> all_punct5("12")
    False
    >>> all_punct5(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct5("")
    True
    """
    search = re.compile(r'[^!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]').search
    return not bool(search(tweet))


def all_punct6(tweet, search=RE_PUNCTUATION.search):
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
    >>> all_punct6("cat")
    False
    >>> all_punct6("cat.")
    False
    >>> all_punct6(".")
    True
    >>> all_punct6("12")
    False
    >>> all_punct6(r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    True
    >>> all_punct6("")
    True
    """
    return not bool(search(tweet))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
