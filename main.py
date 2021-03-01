import parser
from tweet_data_service import TweetDataService
from graphing_service import GraphingService
from pprint import pprint


total_pages = 30
username = 'aoc'


def get_date_dictionary():
    user_timeline = TweetDataService().get_user_timeline(username, total_pages)
    user_tweets = parser.get_tweets(user_timeline)
    return parser.get_date_dictionary(user_tweets)


def get_mood_dictionary():
    return parser.get_mood_dictionary(get_date_dictionary())


mood_dictionary = {
 '2/19/2021': 0.07138888888888889,
 '2/20/2021': 0.08392857142857142,
 '2/21/2021': 0.18928571428571428,
 '2/22/2021': 0.10972222222222222,
 '2/23/2021': 0.21428571428571427,
 '2/24/2021': 0.1625,
 '2/25/2021': 0.35000000000000003,
 '2/26/2021': -0.15,
 '2/28/2021': -0.011904761904761899
}

if __name__ == '__main__':
    # mood_dictionary = get_mood_dictionary()
    pprint(mood_dictionary)
    GraphingService().plot_graph(mood_dictionary, username)

