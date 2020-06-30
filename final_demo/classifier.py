# This is the Sentiment Analyser
# @author James O'Rourke
# @date 08/2016
from nltk.corpus import stopwords
stop = set(stopwords.words())


"""This function builds the corpus of pre analysed tweets"""
def load_corpus() :
    corpus = []
    input_file = open('training.csv')
    for line in input_file:
        (ident, emot, tweet) = line.split(",")
        final_tweet = cleaner(tweet)
        corpus = corpus + [[ident, emot, final_tweet]]
    return corpus


"""This function edits tweets so that only the relevant parts of the tweet are passed into the classifier"""
def cleaner(tweet):
    clean_tweet = tweet.lower().rstrip().lstrip()
    punc_tweet = ''
    for c in clean_tweet:
        if c in ",.!?;#*&@)_(\"-/\\'[]":
            c = ' '
        punc_tweet += c
    neg_tweet = negate(punc_tweet)
    done_tweet = ''
    for word in neg_tweet.split(' '):
        if word in stop:
            word = ''
        done_tweet += (word + ' ')
        final_tweet = done_tweet.lstrip().rstrip()
    return final_tweet


"""This function handles negation. It forms bigrams of words following the word not.
For Example not good becomes not_good"""
def negate(tweet):
    new_tweet = ''
    negation = False
    for word in tweet.split(' '):
        if negation == True:
            word = ('not_' + word)
            negation = False
        if word == 'not':
            negation = True
            word = '@'
        if word == 'nt':
            negation = True
            word = '@'
        if word == 't':
            negation = True
            word = '@'
        if word != '@':
            new_tweet += word + ' '
    return new_tweet

corpus = load_corpus()

"""This function builds a dictionary of words along with the number of times they have appeared in positive or negative
tweets."""
def create_dictionary (corpus):
    total_pos =0
    total_neg = 0
    total_both = 0

    word_freq = {}
    for item in corpus:
        for word in item[2].split():
            word_freq[word] = [0, 0, 0]

    for item in corpus:
        for word in item[2].split():
            [pos, neg, both] = word_freq[word]
            if item[1] == '1':
                pos = pos + 1
                total_pos = total_pos + 1
            elif item[1] == '0':
                neg = neg + 1
                total_neg = total_neg + 1
            both = both + 1
            total_both = total_both + 1
            word_freq[word] = [pos, neg, both]
            word_freq['totals!'] = [total_pos, total_neg, total_both]
    return word_freq


word_dictionary = create_dictionary(corpus)

"""This function classifies tweets as positive or negative. It does this by checking each word against words in the
dictionary. It calculates whether that word has occured in more positive or negative tweets and determines the sentiment
of the word. It then calculates the number of positive and negative words in the tweet and the one with the most defines
the sentiment"""
def classify_tweet(tweet, word_dictionary):
    final_tweet = cleaner(tweet)
    total_pos = 1
    total_neg = 1
    for word in final_tweet.split(' '):
        if word in word_dictionary:
            [pos, neg, total] = word_dictionary[word]
            total_pos = total_pos * pos
            total_neg = total_neg * neg

    [p_pos, p_neg, total_both] = word_dictionary['totals!']
    total_pos = total_pos * (p_pos / total_both)
    total_neg = total_neg * (p_neg / total_both)

    if total_pos > total_neg:
        return 1
    else:
        return 0
