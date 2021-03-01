import parser
from tweet_data_service import TweetDataService
from graphing_service import GraphingService


total_pages = 30
username = 'aoc'


def get_date_dictionary():
    user_timeline = TweetDataService().get_user_timeline(username, total_pages)
    user_tweets = parser.get_tweets(user_timeline)
    return parser.get_date_dictionary(user_tweets)


def get_mood_dictionary():
    return parser.get_mood_dictionary(get_date_dictionary())


mood_dictionary = {
    1613721600.0: -0.08124999999999999,
    1613808000.0: 0.1,
    1613894400.0: 0.0,
    1613980800.0: 0.275,
    1614067200.0: 0.4700000000000001,
    1614153600.0: 0.0,
    1614240000.0: -0.1,
    1614326400.0: -0.15,
    1614499200.0: -0.011904761904761899
}

if __name__ == '__main__':
    # mood_dictionary = get_mood_dictionary()
    # pprint(mood_dictionary)
    GraphingService().plot_graph(mood_dictionary, username)

