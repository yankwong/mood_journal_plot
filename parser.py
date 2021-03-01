import re
from textblob import TextBlob


def get_tweets(statuses):
    tweets = []

    for status in statuses:
        tweets.append(dict(text=status.full_text,
                           created_at=status.created_at.strftime("%-m/%-d/%Y")))
    return tweets


def remove_twitter_url(tweet):
    return re.sub("(?P<url>https?://[^\s]+)", '', tweet)


def get_date_dictionary(tweets):
    date_dictionary = dict()

    for tweet in tweets:
        tweet_date = tweet["created_at"]
        tweet_content = remove_twitter_url(tweet["text"])

        if tweet_date in date_dictionary.keys():
            date_dictionary[tweet_date] += ' ' + tweet_content
        else:
            date_dictionary[tweet_date] = tweet_content

    return date_dictionary


def get_mood_dictionary(date_dictionary):
    mood_dictionary = dict()

    for date in date_dictionary:
        # print('------' + date)
        # print(TextBlob(date_dictionary[date]))
        # print(TextBlob(date_dictionary[date]).sentiment.polarity)
        # print('-----------')
        mood_dictionary[date] = TextBlob(date_dictionary[date]).sentiment.polarity

    return mood_dictionary
