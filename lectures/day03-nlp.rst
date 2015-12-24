**********************************
Day 3: Natural language processing
**********************************

The material for this lecture is adapted from a few sources:

- the free book Natural Language Processing with Python, available from http://www.nltk.org/book
- tutuorials for the `gensim <http://radimrehurek.com/gensim/index.html>`__ Python library

These are great resources if you want to learn more.

NLP refers to computations done on "natural" languages, i.e. naturally
arising human languages such as English (NOT programming languages).

Some applications:

- predicting word completion (e.g. for cellphones)
- computer translation (see http://translationparty.com/ for an illustration of current limitations)
- sentiment analysis
- search (which document is most relevant for a query)

1. Importing example data
=========================

We'll start with some data from the NLTK book.

.. code:: python

    import nltk, string
    #nltk.download() # download book collection (need to do this once)
    from nltk.book import *
    from __future__ import division


.. parsed-literal::

    showing info http://nltk.github.com/nltk_data/


.. code:: python

    # see the name of the example texts
    text1




.. parsed-literal::

    <Text: Moby Dick by Herman Melville 1851>



.. code:: python

    type(text1)




.. parsed-literal::

    nltk.text.Text



Later we'll learn how to create objects of this type. For now, just note
we're working with something that looks like a list of words and
punctuation. (These are called *tokens*.)

.. code:: python

    text1[:10]




.. parsed-literal::

    [u'[',
     u'Moby',
     u'Dick',
     u'by',
     u'Herman',
     u'Melville',
     u'1851',
     u']',
     u'ETYMOLOGY',
     u'.']



.. code:: python

    len(text1) # in tokens




.. parsed-literal::

    260819



2. Word useage: contexts
========================

NLTK has some very useful functions for examining how specific words are
used; that is, examining their context.

concordance: how are words used?
--------------------------------

.. code:: python

    text1.concordance("monstrous") # note that case is ignored


.. parsed-literal::

    Displaying 11 of 11 matches:
    ong the former , one was of a most monstrous size . ... This came towards us , 
    ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
    ll over with a heathenish array of monstrous clubs and spears . Some were thick
    d as you gazed , and wondered what monstrous cannibal and savage could ever hav
    that has survived the flood ; most monstrous and most mountainous ! That Himmal
    they might scout at Moby Dick as a monstrous fable , or still worse and more de
    th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
    ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
    ere to enter upon those still more monstrous stories of them which are to be fo
    ght have been rummaged out of this monstrous cabinet there is no telling . But 
    of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u


.. code:: python

    text2.concordance("monstrous")


.. parsed-literal::

    Displaying 11 of 11 matches:
    . " Now , Palmer , you shall see a monstrous pretty girl ." He immediately went
    your sister is to marry him . I am monstrous glad of it , for then I shall have
    ou may tell your sister . She is a monstrous lucky girl to get him , upon my ho
    k how you will like them . Lucy is monstrous pretty , and so good humoured and 
     Jennings , " I am sure I shall be monstrous glad of Miss Marianne ' s company 
     usual noisy cheerfulness , " I am monstrous glad to see you -- sorry I could n
    t however , as it turns out , I am monstrous glad there was never any thing in 
    so scornfully ! for they say he is monstrous fond of her , as well he may . I s
    possible that she should ." " I am monstrous glad of it . Good gracious ! I hav
    thing of the kind . So then he was monstrous happy , and talked on some time ab
    e very genteel people . He makes a monstrous deal of money , and they keep thei


similar: what words are used in a similar context?
--------------------------------------------------

.. code:: python

    text2.similar("monstrous")


.. parsed-literal::

    very exceedingly so heartily a great good amazingly as sweet
    remarkably extremely vast


common\_contexts: for two words used in similar contexts, see the contexts
--------------------------------------------------------------------------

.. code:: python

    text2.common_contexts(["monstrous", "very"])


.. parsed-literal::

    a_pretty is_pretty a_lucky am_glad be_glad


collocations: see words often used together
-------------------------------------------

.. code:: python

    text1.collocations()


.. parsed-literal::

    Sperm Whale; Moby Dick; White Whale; old man; Captain Ahab; sperm
    whale; Right Whale; Captain Peleg; New Bedford; Cape Horn; cried Ahab;
    years ago; lower jaw; never mind; Father Mapple; cried Stubb; chief
    mate; white whale; ivory leg; one hand


.. code:: python

    text8.collocations()


.. parsed-literal::

    would like; medium build; social drinker; quiet nights; non smoker;
    long term; age open; Would like; easy going; financially secure; fun
    times; similar interests; Age open; weekends away; poss rship; well
    presented; never married; single mum; permanent relationship; slim
    build


3. Word useage: frequencies
===========================

Let's make an alphabetically sorted list of the unique tokens in the
Book of Genesis.

.. code:: python

    unique_tokens = sorted(set(text3))
    unique_tokens[:20]




.. parsed-literal::

    [u'!',
     u"'",
     u'(',
     u')',
     u',',
     u',)',
     u'.',
     u'.)',
     u':',
     u';',
     u';)',
     u'?',
     u'?)',
     u'A',
     u'Abel',
     u'Abelmizraim',
     u'Abidah',
     u'Abide',
     u'Abimael',
     u'Abimelech']



.. code:: python

    len(unique_tokens)




.. parsed-literal::

    2789



We can measure "lexical richness" by dividing the number of unique
tokens by the total number of tokens. Let's compare text1 (Moby Dick) to
text6 (Monty Python).

.. code:: python

    print len(set(text1)) / len(text1)
    print len(set(text6)) / len(text6)


.. parsed-literal::

    0.0740628558502
    0.127659574468


.. code:: python

    text3.count("begat") # count a given token




.. parsed-literal::

    67



.. code:: python

    # note this is better for our purposes than the string version shown earlier
    print "is this".count("is")
    print ["is", "this"].count("is")


.. parsed-literal::

    2
    1


.. code:: python

    # percentage of text made up of specific word
    100 * text3.count("the") / len(text3)




.. parsed-literal::

    5.386024483960325



NLTK provides built-in support for working with frequency distributions
(counts of each unique token).

.. code:: python

    fdist1 = FreqDist(text1)

.. code:: python

    print fdist1


.. parsed-literal::

    <FreqDist with 19317 samples and 260819 outcomes>


.. code:: python

    # extract count for a given token - compare with earlier
    fdist1["the"] 




.. parsed-literal::

    13721



.. code:: python

    # see most commonly occurring words; usually most consist of stop words
    fdist1.most_common(20)




.. parsed-literal::

    [(u',', 18713),
     (u'the', 13721),
     (u'.', 6862),
     (u'of', 6536),
     (u'and', 6024),
     (u'a', 4569),
     (u'to', 4542),
     (u';', 4072),
     (u'in', 3916),
     (u'that', 2982),
     (u"'", 2684),
     (u'-', 2552),
     (u'his', 2459),
     (u'it', 2209),
     (u'I', 2124),
     (u's', 1739),
     (u'is', 1695),
     (u'he', 1661),
     (u'with', 1659),
     (u'was', 1632)]



4. Identifying "important" words
================================

How can we identify "important" or "interesting" words in a text? One
way of qualifying this is to find commonly used long words.

.. code:: python

    # show words that are > 7 characters long and occur more than 7 times
    fdist1 = FreqDist(text1)
    count_long = [(word, fdist1[word]) for word in set(text1) 
                  if len(word) > 7 and fdist1[word] > 7]
    sorted(count_long, key=lambda el: -el[1])




.. parsed-literal::

    [(u'Queequeg', 252),
     (u'Starbuck', 196),
     (u'something', 119),
     (u'Nantucket', 85),
     (u'sometimes', 81),
     (u'harpooneer', 77),
     (u'standing', 73),
     (u'whalemen', 71),
     (u'business', 67),
     (u'together', 64),
     (u'Leviathan', 64),
     (u'themselves', 59),
     (u'therefore', 56),
     (u'peculiar', 56),
     (u'harpooneers', 55),
     (u'Tashtego', 54),
     (u'thousand', 51),
     (u'particular', 49),
     (u'stranger', 48),
     (u'straight', 46),
     (u'touching', 45),
     (u'suddenly', 45),
     (u'whaleman', 44),
     (u'whatever', 44),
     (u'especially', 44),
     (u'creature', 42),
     (u'anything', 41),
     (u'wondrous', 41),
     (u'Steelkilt', 40),
     (u'carpenter', 39),
     (u'distance', 39),
     (u'concerning', 38),
     (u'gentlemen', 37),
     (u'forehead', 37),
     (u'bulwarks', 36),
     (u'Greenland', 35),
     (u'remained', 34),
     (u'previous', 34),
     (u'forecastle', 34),
     (u'thoughts', 34),
     (u'creatures', 34),
     (u'American', 34),
     (u'skeleton', 33),
     (u'completely', 33),
     (u'intervals', 32),
     (u'substance', 31),
     (u'darkness', 31),
     (u'leviathan', 31),
     (u'possible', 30),
     (u'harpoons', 30),
     (u'generally', 30),
     (u'instances', 30),
     (u'altogether', 29),
     (u'possibly', 29),
     (u'mariners', 29),
     (u'swimming', 29),
     (u'strangely', 29),
     (u'entirely', 29),
     (u'question', 29),
     (u'fishermen', 28),
     (u'considering', 28),
     (u'Nevertheless', 27),
     (u'landlord', 27),
     (u'certainly', 27),
     (u'precisely', 27),
     (u'somewhat', 27),
     (u'sideways', 27),
     (u'suspended', 27),
     (u'Fedallah', 27),
     (u'alongside', 27),
     (u'overboard', 27),
     (u'circumstances', 26),
     (u'enormous', 26),
     (u'followed', 26),
     (u'considerable', 26),
     (u'received', 26),
     (u'whiteness', 26),
     (u'yourself', 26),
     (u'otherwise', 26),
     (u'lightning', 26),
     (u'circumstance', 26),
     (u'complete', 25),
     (u'interval', 25),
     (u'thinking', 25),
     (u'cruising', 25),
     (u'floating', 24),
     (u'different', 24),
     (u'midnight', 24),
     (u'afterwards', 24),
     (u'following', 23),
     (u'somewhere', 23),
     (u'strength', 23),
     (u'striking', 23),
     (u'commanded', 23),
     (u'regarded', 23),
     (u'speaking', 23),
     (u'nevertheless', 23),
     (u'shipmates', 22),
     (u'Nantucketer', 22),
     (u'wonderful', 22),
     (u'answered', 22),
     (u'descried', 22),
     (u'windward', 22),
     (u'original', 21),
     (u'invested', 21),
     (u'terrible', 21),
     (u'magnitude', 21),
     (u'windlass', 21),
     (u'gentleman', 20),
     (u'directly', 20),
     (u'officers', 20),
     (u'attached', 20),
     (u'gigantic', 20),
     (u'according', 20),
     (u'sleeping', 20),
     (u'repeated', 20),
     (u'everything', 20),
     (u'slightest', 20),
     (u'separate', 20),
     (u'profound', 20),
     (u'solitary', 19),
     (u'Atlantic', 19),
     (u'ordinary', 19),
     (u'presented', 19),
     (u'vicinity', 19),
     (u'pointing', 19),
     (u'blacksmith', 19),
     (u'important', 19),
     (u'beginning', 19),
     (u'Meantime', 19),
     (u'concluded', 19),
     (u'captains', 19),
     (u'cannibal', 18),
     (u'revealed', 18),
     (u'Christian', 18),
     (u'observed', 18),
     (u'nameless', 18),
     (u'mentioned', 18),
     (u'instance', 18),
     (u'precious', 18),
     (u'advancing', 18),
     (u'interest', 18),
     (u'children', 18),
     (u'difference', 18),
     (u'prodigious', 18),
     (u'regularly', 18),
     (u'elephant', 17),
     (u'instantly', 17),
     (u'opposite', 17),
     (u'inserted', 17),
     (u'likewise', 17),
     (u'tomahawk', 17),
     (u'muttered', 17),
     (u'lowering', 17),
     (u'previously', 17),
     (u'understand', 17),
     (u'continually', 17),
     (u'captured', 17),
     (u'doubloon', 17),
     (u'spermaceti', 16),
     (u'originally', 16),
     (u'Meanwhile', 16),
     (u'binnacle', 16),
     (u'commander', 16),
     (u'civilized', 16),
     (u'actually', 16),
     (u'starboard', 16),
     (u'crossing', 16),
     (u'encountered', 16),
     (u'encounter', 16),
     (u'distinct', 16),
     (u'pleasant', 16),
     (u'dropping', 16),
     (u'scientific', 16),
     (u'uncommon', 16),
     (u'furnished', 16),
     (u'happened', 16),
     (u'breaking', 16),
     (u'numerous', 16),
     (u'stricken', 16),
     (u'hitherto', 16),
     (u'unaccountable', 16),
     (u'thousands', 16),
     (u'exclaimed', 15),
     (u'troubled', 15),
     (u'consider', 15),
     (u'marvellous', 15),
     (u'wrinkles', 15),
     (u'carrying', 15),
     (u'impossible', 15),
     (u'horizontal', 15),
     (u'invisible', 15),
     (u'employed', 15),
     (u'supposed', 15),
     (u'ourselves', 15),
     (u'exceedingly', 15),
     (u'position', 15),
     (u'merchant', 15),
     (u'disappeared', 15),
     (u'direction', 15),
     (u'latitudes', 15),
     (u'remember', 15),
     (u'watching', 15),
     (u'perilous', 15),
     (u'returned', 14),
     (u'wrinkled', 14),
     (u'continued', 14),
     (u'immortal', 14),
     (u'simultaneously', 14),
     (u'continual', 14),
     (u'whenever', 14),
     (u'terrific', 14),
     (u'probably', 14),
     (u'frequently', 14),
     (u'immediately', 14),
     (u'character', 14),
     (u'customary', 14),
     (u'silently', 14),
     (u'declared', 14),
     (u'critical', 14),
     (u'departed', 14),
     (u'considered', 14),
     (u'horrible', 14),
     (u'occasionally', 14),
     (u'perceived', 14),
     (u'tormented', 14),
     (u'anywhere', 14),
     (u'superior', 14),
     (u'slightly', 13),
     (u'sounding', 13),
     (u'breakfast', 13),
     (u'ponderous', 13),
     (u'pictures', 13),
     (u'dangerous', 13),
     (u'shoulders', 13),
     (u'swinging', 13),
     (u'belonged', 13),
     (u'indirectly', 13),
     (u'trowsers', 13),
     (u'practical', 13),
     (u'individual', 13),
     (u'presently', 13),
     (u'latitude', 13),
     (u'resolved', 13),
     (u'remarkable', 13),
     (u'swallowed', 13),
     (u'quantity', 13),
     (u'subsequent', 13),
     (u'tapering', 12),
     (u'bursting', 12),
     (u'downwards', 12),
     (u'prepared', 12),
     (u'contrast', 12),
     (u'murmured', 12),
     (u'naturally', 12),
     (u'ambergris', 12),
     (u'enchanted', 12),
     (u'external', 12),
     (u'centuries', 12),
     (u'conscience', 12),
     (u'unearthly', 12),
     (u'sweeping', 12),
     (u'meanwhile', 12),
     (u'exceeding', 12),
     (u'connected', 12),
     (u'desperate', 12),
     (u'reaching', 12),
     (u'doubtless', 12),
     (u'shoulder', 12),
     (u'involuntarily', 12),
     (u'interior', 12),
     (u'countenance', 12),
     (u'mountain', 12),
     (u'stranded', 12),
     (u'knowledge', 12),
     (u'greatest', 12),
     (u'glancing', 12),
     (u'contrary', 12),
     (u'NANTUCKET', 11),
     (u'demanded', 11),
     (u'fastened', 11),
     (u'spiritual', 11),
     (u'infallibly', 11),
     (u'peculiarities', 11),
     (u'concluding', 11),
     (u'commotion', 11),
     (u'lengthwise', 11),
     (u'elevated', 11),
     (u'elsewhere', 11),
     (u'indifferent', 11),
     (u'convenient', 11),
     (u'additional', 11),
     (u'receiving', 11),
     (u'valuable', 11),
     (u'temporary', 11),
     (u'experienced', 11),
     (u'spouting', 11),
     (u'vengeance', 11),
     (u'features', 11),
     (u'reference', 11),
     (u'monomaniac', 11),
     (u'fashioned', 11),
     (u'perpendicular', 11),
     (u'naturalists', 11),
     (u'whispered', 11),
     (u'invariably', 11),
     (u'helmsman', 11),
     (u'significant', 11),
     (u'appearance', 11),
     (u'straightway', 11),
     (u'excellent', 11),
     (u'blackness', 11),
     (u'shipmate', 11),
     (u'advanced', 11),
     (u'steadily', 11),
     (u'indispensable', 11),
     (u'Therefore', 11),
     (u'barbaric', 11),
     (u'beholding', 11),
     (u'strongly', 11),
     (u'included', 11),
     (u'prolonged', 11),
     (u'hoisting', 11),
     (u'vocation', 11),
     (u'Guernsey', 11),
     (u'uncertain', 10),
     (u'bringing', 10),
     (u'remotest', 10),
     (u'foremost', 10),
     (u'superstitious', 10),
     (u'leviathans', 10),
     (u'impressions', 10),
     (u'appalling', 10),
     (u'experience', 10),
     (u'possession', 10),
     (u'retained', 10),
     (u'occurred', 10),
     (u'steering', 10),
     (u'mainmast', 10),
     (u'grinning', 10),
     (u'striving', 10),
     (u'Nantucketers', 10),
     (u'mysterious', 10),
     (u'discovered', 10),
     (u'moreover', 10),
     (u'downward', 10),
     (u'comrades', 10),
     (u'velocity', 10),
     (u'throwing', 10),
     (u'Jeroboam', 10),
     (u'remaining', 10),
     (u'venerable', 10),
     (u'ignorant', 10),
     (u'uplifted', 10),
     (u'curiosity', 10),
     (u'surprise', 10),
     (u'ignorance', 10),
     (u'appeared', 10),
     (u'entitled', 10),
     (u'afternoon', 10),
     (u'headsman', 10),
     (u'elephants', 10),
     (u'murderous', 10),
     (u'carefully', 10),
     (u'smallest', 10),
     (u'yesterday', 10),
     (u'Moreover', 10),
     (u'stripped', 10),
     (u'occasion', 10),
     (u'inferior', 10),
     (u'domestic', 10),
     (u'consternation', 10),
     (u'compasses', 10),
     (u'supplied', 10),
     (u'Japanese', 10),
     (u'discovery', 10),
     (u'Porpoise', 10),
     (u'landsmen', 10),
     (u'gradually', 10),
     (u'eastward', 10),
     (u'articles', 10),
     (u'monstrous', 10),
     (u'hovering', 10),
     (u'violently', 9),
     (u'extremity', 9),
     (u'detached', 9),
     (u'considerably', 9),
     (u'apparition', 9),
     (u'expression', 9),
     (u'combined', 9),
     (u'intended', 9),
     (u'revolving', 9),
     (u'shuddering', 9),
     (u'hereafter', 9),
     (u'approaching', 9),
     (u'monsters', 9),
     (u'influence', 9),
     (u'occasional', 9),
     (u'cannibals', 9),
     (u'involved', 9),
     (u'singular', 9),
     (u'sufficiently', 9),
     (u'traveller', 9),
     (u'withstand', 9),
     (u'temporarily', 9),
     (u'accursed', 9),
     (u'daylight', 9),
     (u'unspeakable', 9),
     (u'sparkling', 9),
     (u'larboard', 9),
     (u'accounted', 9),
     (u'comfortable', 9),
     (u'independent', 9),
     (u'seemingly', 9),
     (u'intently', 9),
     (u'strained', 9),
     (u'intolerable', 9),
     (u'confidential', 9),
     (u'relieved', 9),
     (u'forgotten', 9),
     (u'Commodore', 9),
     (u'properly', 9),
     (u'Scoresby', 9),
     (u'projecting', 9),
     (u'vigorous', 9),
     (u'principle', 9),
     (u'particulars', 9),
     (u'recognised', 9),
     (u'occupied', 9),
     (u'sensible', 9),
     (u'devilish', 9),
     (u'malicious', 9),
     (u'stretched', 9),
     (u'everlasting', 9),
     (u'movement', 9),
     (u'scattered', 9),
     (u'throughout', 9),
     (u'reserved', 9),
     (u'apparently', 9),
     (u'tremendous', 9),
     (u'mystical', 9),
     (u'destroyed', 9),
     (u'Mediterranean', 9),
     (u'stopping', 9),
     (u'descending', 9),
     (u'succeeded', 9),
     (u'tumultuous', 9),
     (u'abounding', 9),
     (u'tambourine', 9),
     (u'accounts', 9),
     (u'directions', 9),
     (u'presumed', 9),
     (u'freighted', 9),
     (u'activity', 9),
     (u'attention', 9),
     (u'contrasting', 9),
     (u'inclined', 9),
     (u'dripping', 9),
     (u'imperial', 9),
     (u'levelled', 9),
     (u'Sebastian', 9),
     (u'thrusting', 9),
     (u'incredible', 9),
     (u'whalebone', 8),
     (u'specially', 8),
     (u'conscious', 8),
     (u'contrivances', 8),
     (u'lingering', 8),
     (u'elements', 8),
     (u'beautiful', 8),
     (u'operation', 8),
     (u'taffrail', 8),
     (u'connexion', 8),
     (u'measureless', 8),
     (u'hammered', 8),
     (u'concerned', 8),
     (u'consideration', 8),
     (u'transparent', 8),
     (u'conclude', 8),
     (u'Bulkington', 8),
     (u'compared', 8),
     (u'perpendicularly', 8),
     (u'glittering', 8),
     (u'clinging', 8),
     (u'reasonable', 8),
     (u'miserable', 8),
     (u'traditions', 8),
     (u'slouched', 8),
     (u'preliminary', 8),
     (u'vitality', 8),
     (u'bestowed', 8),
     (u'harpooned', 8),
     (u'inscrutable', 8),
     (u'Heidelburgh', 8),
     (u'moonlight', 8),
     (u'surrounded', 8),
     (u'coloured', 8),
     (u'Wherefore', 8),
     (u'unnatural', 8),
     (u'fountain', 8),
     (u'infinite', 8),
     (u'obedience', 8),
     (u'described', 8),
     (u'authority', 8),
     (u'melancholy', 8),
     (u'including', 8),
     (u'popularly', 8),
     (u'infernal', 8),
     (u'scarcely', 8),
     (u'mistaken', 8),
     (u'phantoms', 8),
     (u'instinct', 8),
     (u'universal', 8),
     (u'solemnly', 8),
     (u'Consider', 8),
     (u'perceive', 8),
     (u'hundreds', 8),
     (u'tattooed', 8),
     (u'historical', 8),
     (u'Canallers', 8),
     (u'interesting', 8),
     (u'distinctly', 8),
     (u'eventually', 8),
     (u'starting', 8),
     (u'archangel', 8),
     (u'particularly', 8),
     (u'withdrawing', 8),
     (u'motionless', 8),
     (u'bowsprit', 8),
     (u'snatching', 8),
     (u'intensity', 8),
     (u'judgment', 8),
     (u'proceeds', 8),
     (u'comparatively', 8),
     (u'published', 8),
     (u'hopeless', 8),
     (u'containing', 8),
     (u'specific', 8),
     (u'backward', 8),
     (u'obliquely', 8),
     (u'gunwales', 8),
     (u'fearless', 8),
     (u'belonging', 8),
     (u'observing', 8),
     (u'vertebrae', 8),
     (u'mechanically', 8),
     (u'mountains', 8),
     (u'narrative', 8),
     (u'submerged', 8),
     (u'material', 8),
     (u'respects', 8),
     (u'landsman', 8),
     (u'grandeur', 8),
     (u'intention', 8),
     (u'eagerness', 8)]



Approaching this from the opposite direction, we might *remove* commonly
occuring short words. These are also known as *stop words*.

.. code:: python

    from nltk.corpus import stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords[:10]




.. parsed-literal::

    [u'i',
     u'me',
     u'my',
     u'myself',
     u'we',
     u'our',
     u'ours',
     u'ourselves',
     u'you',
     u'your']



.. code:: python

    # Find most frequently occurring words, removing stop words first
    content1 = [word for word in text1 if word.lower() not in stopwords]
    fdist1 = FreqDist(content1)
    fdist1.most_common(20)




.. parsed-literal::

    [(u',', 18713),
     (u'.', 6862),
     (u';', 4072),
     (u"'", 2684),
     (u'-', 2552),
     (u'"', 1478),
     (u'!', 1269),
     (u'--', 1070),
     (u'whale', 906),
     (u'one', 889),
     (u'?', 637),
     (u'like', 624),
     (u'upon', 538),
     (u'man', 508),
     (u'ship', 507),
     (u'Ahab', 501),
     (u'."', 489),
     (u'ye', 460),
     (u'old', 436),
     (u'sea', 433)]



We'll come back to the question of how to remove tokens that are nothing
but punctuation.

5. Working with raw text data
=============================

Now we'll grab some text from the web. Project Gutenberg has an online
collection of free ebooks in various formats, including plain text.

.. code:: python

    import urllib
    
    # link for Crime and Punishment
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    
    response = urllib.urlopen(url)
    raw = response.read().decode('utf8')

.. code:: python

    type(raw)




.. parsed-literal::

    unicode



.. code:: python

    # Length - in characters, not tokens
    len(raw)




.. parsed-literal::

    1176896



.. code:: python

    raw[:500]




.. parsed-literal::

    u'The Project Gutenberg EBook of Crime and Punishment, by Fyodor Dostoevsky\r\n\r\nThis eBook is for the use of anyone anywhere at no cost and with\r\nalmost no restrictions whatsoever.  You may copy it, give it away or\r\nre-use it under the terms of the Project Gutenberg License included\r\nwith this eBook or online at www.gutenberg.org\r\n\r\n\r\nTitle: Crime and Punishment\r\n\r\nAuthor: Fyodor Dostoevsky\r\n\r\nRelease Date: March 28, 2006 [EBook #2554]\r\n[Last updated: November 15, 2011]\r\n\r\nLanguage: English\r\n\r\nChar'



Manually searching for the content
----------------------------------

I opened the link from the Project Gutenburg website to look at the text
we just downloaded. There's an introduction I don't want to include.
Scrolling down, I see that the book begins with the words "PART I."
There's also some copyright information at the end, following the words
"End of Project Gutenberg's Crime and Punishment, by Fyodor Dostoevsky."

.. code:: python

    raw.find("PART I") # first instance




.. parsed-literal::

    5338



.. code:: python

    raw[5338:5500]




.. parsed-literal::

    u'PART I\r\n\r\n\r\n\r\nCHAPTER I\r\n\r\nOn an exceptionally hot evening early in July a young man came out of\r\nthe garret in which he lodged in S. Place and walked slowly, as '



.. code:: python

    raw.rfind("End of Project Gutenberg's Crime") # last instance




.. parsed-literal::

    1157746



.. code:: python

    raw[1157600:1157746]




.. parsed-literal::

    u'd into another, of his initiation into a new unknown life.\r\nThat might be the subject of a new story, but our present story is\r\nended.\r\n\r\n\r\n\r\n\r\n\r\n'



.. code:: python

    raw = raw[5338:1157746]

Tokenization
------------

Tokenizers divide strings into lists of substrings. Usually we do this
because we want to split a string into sentences or words. This topic is
complex and NLTK has some built-in functions we can use, without delving
too much into the algorithms behind them.

.. code:: python

    raw[:500]




.. parsed-literal::

    u'PART I\r\n\r\n\r\n\r\nCHAPTER I\r\n\r\nOn an exceptionally hot evening early in July a young man came out of\r\nthe garret in which he lodged in S. Place and walked slowly, as though\r\nin hesitation, towards K. bridge.\r\n\r\nHe had successfully avoided meeting his landlady on the staircase. His\r\ngarret was under the roof of a high, five-storied house and was more\r\nlike a cupboard than a room. The landlady who provided him with garret,\r\ndinners, and attendance, lived on the floor below, and every time\r\nhe went out'



One simple way to tokenize is with split.

.. code:: python

    # default separator is any whitespace
    raw[:500].split()




.. parsed-literal::

    [u'PART',
     u'I',
     u'CHAPTER',
     u'I',
     u'On',
     u'an',
     u'exceptionally',
     u'hot',
     u'evening',
     u'early',
     u'in',
     u'July',
     u'a',
     u'young',
     u'man',
     u'came',
     u'out',
     u'of',
     u'the',
     u'garret',
     u'in',
     u'which',
     u'he',
     u'lodged',
     u'in',
     u'S.',
     u'Place',
     u'and',
     u'walked',
     u'slowly,',
     u'as',
     u'though',
     u'in',
     u'hesitation,',
     u'towards',
     u'K.',
     u'bridge.',
     u'He',
     u'had',
     u'successfully',
     u'avoided',
     u'meeting',
     u'his',
     u'landlady',
     u'on',
     u'the',
     u'staircase.',
     u'His',
     u'garret',
     u'was',
     u'under',
     u'the',
     u'roof',
     u'of',
     u'a',
     u'high,',
     u'five-storied',
     u'house',
     u'and',
     u'was',
     u'more',
     u'like',
     u'a',
     u'cupboard',
     u'than',
     u'a',
     u'room.',
     u'The',
     u'landlady',
     u'who',
     u'provided',
     u'him',
     u'with',
     u'garret,',
     u'dinners,',
     u'and',
     u'attendance,',
     u'lived',
     u'on',
     u'the',
     u'floor',
     u'below,',
     u'and',
     u'every',
     u'time',
     u'he',
     u'went',
     u'out']



.. code:: python

    from nltk import word_tokenize
    
    tokens = word_tokenize(raw)
    type(tokens)




.. parsed-literal::

    list



.. code:: python

    len(tokens)




.. parsed-literal::

    250031



.. code:: python

    print tokens[:50]


.. parsed-literal::

    [u'PART', u'I', u'CHAPTER', u'I', u'On', u'an', u'exceptionally', u'hot', u'evening', u'early', u'in', u'July', u'a', u'young', u'man', u'came', u'out', u'of', u'the', u'garret', u'in', u'which', u'he', u'lodged', u'in', u'S.', u'Place', u'and', u'walked', u'slowly', u',', u'as', u'though', u'in', u'hesitation', u',', u'towards', u'K.', u'bridge', u'.', u'He', u'had', u'successfully', u'avoided', u'meeting', u'his', u'landlady', u'on', u'the', u'staircase']


The word\_tokenize function is based on the `Treebank tokenization
algorithm <http://www.cis.upenn.edu/~treebank/tokenization.html>`__. One
advantage of this algorithm is that it handles contractions in an
appropriate way, which is tricky to do for all cases using regular
expressions.

.. code:: python

    word_tokenize("I've been to the U.S. twice. I don't plan to go back.")




.. parsed-literal::

    ['I',
     "'ve",
     'been',
     'to',
     'the',
     'U.S.',
     'twice',
     '.',
     'I',
     'do',
     "n't",
     'plan',
     'to',
     'go',
     'back',
     '.']



.. code:: python

    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+') # one or more word characters
    tokenizer.tokenize("I've been to the U.S. twice. I don't plan to go back.")




.. parsed-literal::

    ['I',
     've',
     'been',
     'to',
     'the',
     'U',
     'S',
     'twice',
     'I',
     'don',
     't',
     'plan',
     'to',
     'go',
     'back']



One refinement we might want to make is to remove the tokens that
consist *only* of punctuation.

.. code:: python

    string.punctuation




.. parsed-literal::

    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'



.. code:: python

    def all_punct(x):
        return(all([char in string.punctuation for char in x]))
    
    def my_tokenize(text):
        init_words = word_tokenize(text)
        return([w for w in init_words if not all_punct(w)])

.. code:: python

    tokens = my_tokenize(raw)
    print tokens[:50]


.. parsed-literal::

    [u'PART', u'I', u'CHAPTER', u'I', u'On', u'an', u'exceptionally', u'hot', u'evening', u'early', u'in', u'July', u'a', u'young', u'man', u'came', u'out', u'of', u'the', u'garret', u'in', u'which', u'he', u'lodged', u'in', u'S.', u'Place', u'and', u'walked', u'slowly', u'as', u'though', u'in', u'hesitation', u'towards', u'K.', u'bridge', u'He', u'had', u'successfully', u'avoided', u'meeting', u'his', u'landlady', u'on', u'the', u'staircase', u'His', u'garret', u'was']


Exercise: 1. Write a new function called any\_punct that checks whether
a string contains any punctuation. 2. Use this function to create a set
of tokens containing punctuation from the example above. Do you see any
examples of tokens that suggest further improvements we could make?

Creating an nltk.Text object
----------------------------

Now we can create an nltk.Text object and use all the NLTK functions for
processing.

.. code:: python

    text = nltk.Text(tokens)
    type(text)




.. parsed-literal::

    nltk.text.Text



.. code:: python

    print text[:20]


.. parsed-literal::

    [u'PART', u'I', u'CHAPTER', u'I', u'On', u'an', u'exceptionally', u'hot', u'evening', u'early', u'in', u'July', u'a', u'young', u'man', u'came', u'out', u'of', u'the', u'garret']


.. code:: python

    text.collocations()


.. parsed-literal::

    Katerina Ivanovna; Pyotr Petrovitch; Pulcheria Alexandrovna; Avdotya
    Romanovna; Rodion Romanovitch; Marfa Petrovna; Sofya Semyonovna; old
    woman; Porfiry Petrovitch; Amalia Ivanovna; great deal; Nikodim
    Fomitch; young man; Ilya Petrovitch; n't know; Dmitri Prokofitch;
    Andrey Semyonovitch; Hay Market; Good heavens; police station


.. code:: python

    content = [w for w in text if w.lower() not in stopwords]
    fdist = FreqDist(content)
    fdist.most_common(10)




.. parsed-literal::

    [(u"'s", 1620),
     (u"n't", 1065),
     (u'Raskolnikov', 778),
     (u'would', 587),
     (u'one', 576),
     (u'know', 527),
     (u'could', 521),
     (u'said', 517),
     (u'man', 470),
     (u'like', 449)]



6. Vector representations
=========================

Much of advanced text processing is based on creating a vector
representation of each text. Think of each element of the vector being a
real number representing the answer to a specific question.

For example, we could have a dictionary of all possible words and then a
long vector counting the number of times each word occurs in a text.
Note that this vector would be *sparse*, i.e. containing many zeroes.
Efficient implementatations of text-mining algorithms take advantage of
this sparsity.

For working with efficient vector representations, we can use the
`gensim <http://radimrehurek.com/gensim/index.html>`__ Python library.
I'm going to switch over now to using a simple example from one of the
gensim tutorials.

Imagine that the following are titles of academic papers. The goal is to
return the best matching paper for a particular search string.

.. code:: python

    from gensim import corpora, models, similarities
    documents = ["Human machine interface for lab abc computer applications",
                  "A survey of user opinion of computer system response time",
                  "The EPS user interface management system",
                  "System and human system engineering testing of EPS",
                  "Relation of user perceived response time to error measurement",
                  "The generation of random binary unordered trees",
                  "The intersection graph of paths in trees",
                  "Graph minors IV Widths of trees and well quasi ordering",
                  "Graph minors A survey"]

.. code:: python

    # remove common words and tokenize
    stoplist = set('for a of the and to in'.split()) # an abbreviated list of stop words
    texts = [[word for word in document.lower().split() 
              if word not in stoplist]
              for document in documents]
    texts




.. parsed-literal::

    [['human', 'machine', 'interface', 'lab', 'abc', 'computer', 'applications'],
     ['survey', 'user', 'opinion', 'computer', 'system', 'response', 'time'],
     ['eps', 'user', 'interface', 'management', 'system'],
     ['system', 'human', 'system', 'engineering', 'testing', 'eps'],
     ['relation', 'user', 'perceived', 'response', 'time', 'error', 'measurement'],
     ['generation', 'random', 'binary', 'unordered', 'trees'],
     ['intersection', 'graph', 'paths', 'trees'],
     ['graph', 'minors', 'iv', 'widths', 'trees', 'well', 'quasi', 'ordering'],
     ['graph', 'minors', 'survey']]



.. code:: python

    # find the unique words
    dictionary = corpora.Dictionary(texts)
    print dictionary


.. parsed-literal::

    Dictionary(35 unique tokens: [u'minors', u'generation', u'testing', u'iv', u'engineering']...)


.. code:: python

    print dictionary.token2id # numbers represent ids, not counts


.. parsed-literal::

    {u'minors': 30, u'generation': 22, u'testing': 16, u'iv': 29, u'engineering': 15, u'computer': 2, u'relation': 20, u'human': 3, u'measurement': 18, u'unordered': 25, u'binary': 21, u'abc': 0, u'ordering': 31, u'graph': 26, u'system': 10, u'machine': 6, u'quasi': 32, u'random': 23, u'paths': 28, u'error': 17, u'trees': 24, u'lab': 5, u'applications': 1, u'management': 14, u'user': 12, u'interface': 4, u'intersection': 27, u'response': 8, u'perceived': 19, u'widths': 34, u'well': 33, u'eps': 13, u'survey': 9, u'time': 11, u'opinion': 7}


.. code:: python

    # for a new string, convert to "bag of words" representation using the dictionary
    dictionary.doc2bow("human computer interaction survey computer".split())




.. parsed-literal::

    [(2, 2), (3, 1), (9, 1)]



Note that the word "interaction" is not in the dictionary and is
ignored.

.. code:: python

    # convert all documents
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpus




.. parsed-literal::

    [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)],
     [(2, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1)],
     [(4, 1), (10, 1), (12, 1), (13, 1), (14, 1)],
     [(3, 1), (10, 2), (13, 1), (15, 1), (16, 1)],
     [(8, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1), (20, 1)],
     [(21, 1), (22, 1), (23, 1), (24, 1), (25, 1)],
     [(24, 1), (26, 1), (27, 1), (28, 1)],
     [(24, 1), (26, 1), (29, 1), (30, 1), (31, 1), (32, 1), (33, 1), (34, 1)],
     [(9, 1), (26, 1), (30, 1)]]



A *term-document matrix* has rows representing words/tokens and columns
representing documents. Each element counts the number of times a
particular word occurs in a particular document. We can think of the
corpus object above as representing the term-document matrix in a format
that discards all the zero entries.

It is common to divide each entry by a function of the number of times
the word occurs in the entire corpus (collection of documents). This
calculation is called TF-IDF, which stands for "term frequency x inverse
document frequency."

Let's see the options by looking at the help for models.TfidfModel in
gensim.

.. code:: python

    models.TfidfModel?

.. code:: python

    tfidf = models.TfidfModel(corpus, normalize=True)
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)


.. parsed-literal::

    [(0, 0.4301019571350565), (1, 0.4301019571350565), (2, 0.2944198962221451), (3, 0.2944198962221451), (4, 0.2944198962221451), (5, 0.4301019571350565), (6, 0.4301019571350565)]
    [(2, 0.3726494271826947), (7, 0.5443832091958983), (8, 0.3726494271826947), (9, 0.3726494271826947), (10, 0.27219160459794917), (11, 0.3726494271826947), (12, 0.27219160459794917)]
    [(4, 0.438482464916089), (10, 0.32027755044706185), (12, 0.32027755044706185), (13, 0.438482464916089), (14, 0.6405551008941237)]
    [(3, 0.3449874408519962), (10, 0.5039733231394895), (13, 0.3449874408519962), (15, 0.5039733231394895), (16, 0.5039733231394895)]
    [(8, 0.30055933182961736), (11, 0.30055933182961736), (12, 0.21953536176370683), (17, 0.43907072352741366), (18, 0.43907072352741366), (19, 0.43907072352741366), (20, 0.43907072352741366)]
    [(21, 0.48507125007266594), (22, 0.48507125007266594), (23, 0.48507125007266594), (24, 0.24253562503633297), (25, 0.48507125007266594)]
    [(24, 0.31622776601683794), (26, 0.31622776601683794), (27, 0.6324555320336759), (28, 0.6324555320336759)]
    [(24, 0.20466057569885868), (26, 0.20466057569885868), (29, 0.40932115139771735), (30, 0.2801947048062438), (31, 0.40932115139771735), (32, 0.40932115139771735), (33, 0.40932115139771735), (34, 0.40932115139771735)]
    [(9, 0.6282580468670046), (26, 0.45889394536615247), (30, 0.6282580468670046)]


Now we're ready to implement the search. First we need to convert our
query to the TF-IDF representation.

.. code:: python

    doc = "Human computer interaction"
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_tfidf = tfidf[vec_bow]
    print(vec_tfidf)


.. parsed-literal::

    [(2, 0.7071067811865476), (3, 0.7071067811865476)]


Now we need a way of determining which of the article titles are
"closest" to our query. Think of our vectors in high-dimensional space.
We'll use the cosine of the angle between each pair of vectors as our
similarity metric.

.. code:: python

    index = similarities.MatrixSimilarity(corpus_tfidf)
    sims = index[vec_tfidf] # perform a similarity query against the corpus
    print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples


.. parsed-literal::

    WARNING:gensim.similarities.docsim:scanning corpus to determine the number of features (consider setting `num_features` explicitly)


.. parsed-literal::

    [(0, 0.4163726), (1, 0.26350293), (2, 0.0), (3, 0.24394296), (4, 0.0), (5, 0.0), (6, 0.0), (7, 0.0), (8, 0.0)]


.. code:: python

    sorted(enumerate(sims), key=lambda item: -item[1])




.. parsed-literal::

    [(0, 0.4163726),
     (1, 0.26350293),
     (3, 0.24394296),
     (2, 0.0),
     (4, 0.0),
     (5, 0.0),
     (6, 0.0),
     (7, 0.0),
     (8, 0.0)]



Various other transformations of the basic bag-of-words representation
have been proposed. For example, Latent Semantic Indexing (LSI) is based
on taking the SVD of either the term-document matrix or the TF-IDF
matrix. See the list of avaiable transformations in gensim
`here <http://radimrehurek.com/gensim/tut2.html>`__.
