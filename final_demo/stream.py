import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from classifier import *
from twitter_api import *
from results import *
from nltk.corpus import stopwords

stop = set(stopwords.words())
corpus = load_corpus()
word_dictionary = create_dictionary(corpus)
final_results = []
final_count = []
tweets = []
progress = 0


class MyListener(StreamListener):
    """This function is the init function for the stream"""
    def __init__(self, counter):
        super(MyListener, self).__init__()
        self.opinions = []
        self.counter = 0
        self.count = counter
        self.results = []
        self.tweets = []
        self.tagged_tweets = []
    """This function processes the data streamed by the MyListener class. It saves each tweet and calls various functions
    on them"""
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        opinion = classify_tweet(tweet, word_dictionary)
        self.tweets.append(tweet)
        self.tagged_tweets += (tokenize(tweet))
        self.opinions += str(opinion)
        self.counter += 1
        if self.counter == self.count:
            tweets.append(self.tweets)
            self.results = (calc(self.opinions))
            progress = int(self.counter / self.count * 100)
            print(str(progress) + '%')
            print(self.counter)
            del final_results[:]
            final_results.append(str(self.results))
            del final_count[:]
            final_count.append(str(findtags('JJ', self.tagged_tweets)))
            return False
        else:
            progress = int(self.counter / self.count * 100)
            print(str(progress)+'%')
            print(self.counter)
            return True
    """"This function displays an error if one occurs"""
    def on_error(self, status):
        print(status)


"""This function starts the stream and sets the search term and number of tweets"""
def run(searchterm, counter):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, MyListener(counter))
    twitter_stream.filter(track=[searchterm])

