import nltk
from classifier import cleaner


"""This function calculates and displays the number of positive and negative tweets in a given list of analysed
tweets"""
def calc(tweets):
    pos = 0
    neg = 0
    total = 0
    for (opinion) in tweets:
        if opinion == str(1):
            pos += 1
        elif opinion == str(0):
            neg += 1
        total += 1
    return 'Out of ' + str(total) + ' tweets, ' + str(pos) + ' were positive and ' + str(neg) + ' were negative.'


def tokenize(tweet):
    """This function takes in a corpus of tweets and builds a list of POS tagged tweets"""
    try:
        tagged_tweet = []
        cleaned_tweet = cleaner(tweet)
        for word in cleaned_tweet.split(' '):
            words = nltk.word_tokenize(word)
            tagged = nltk.pos_tag(words)
            tagged_tweet += tagged
        return tagged_tweet
    except Exception as e:
            print(str(e))


def findtags(tag_prefix, tagged_corpus):
    """This function calculates and displays the highest used words with a given tag. It then presents them."""
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_corpus
                                   if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(5)) for tag in cfd.conditions())


def to_string(tweets):
    for tweet in tweets:
        return str(tweet)

