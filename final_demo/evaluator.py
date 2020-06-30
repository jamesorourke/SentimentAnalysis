from classifier import *
"""This function calculates the accuracy of the classifier function by comparing the returned sentiment of a
    tweet with its known sentiment. It then returns the % of accurate sentiment analyses"""
def evaluate(word_dictionary):
    count = 0
    correct = 0
    input_file = open('test.csv')
    for line in input_file:
        (ident, emot, tweet) = line.split(',')
        final_tweet = cleaner(tweet)
        guess = classify_tweet(final_tweet, word_dictionary)
        if guess == int(emot):
            correct += 1
        if guess != int(emot):
            print(tweet, final_tweet, guess)
        count += 1
    score = round(correct/count * 100)
    print("classifier is " + str(score) + "% correct.")

print(evaluate(word_dictionary))