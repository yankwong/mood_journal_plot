import parser
from tweet_data_service import TweetDataService
from graphing_service import GraphingService


total_pages = 40
# username = 'aoc'


def get_date_dictionary():
    user_timeline = TweetDataService().get_user_timeline(username, total_pages)
    user_tweets = parser.get_tweets(user_timeline)
    return parser.get_date_dictionary(user_tweets)


def get_mood_dictionary():
    return parser.get_mood_dictionary(get_date_dictionary())


if __name__ == '__main__':
    username = input("Please input the twitter handle: @")
    print('Analyzing... please wait...')
    mood_dictionary = get_mood_dictionary()
    GraphingService().plot_graph(mood_dictionary, username)

