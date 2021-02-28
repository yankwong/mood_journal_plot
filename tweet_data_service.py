import os
import tweepy
from dotenv import load_dotenv


class TweetDataService:

    def __init__(self):
        self.__get_tweepy_api()

    def __get_tweepy_api(self):
        load_dotenv()
        api_key = os.getenv('TWITTER_API_KEY')
        api_secret = os.getenv('TWITTER_API_SECRET')
        api_token = os.getenv('TWITTER_ACCESS_TOKEN')
        api_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(api_token, api_token_secret)

        self.tweepy_api = tweepy.API(auth)

    def get_user_timeline(self, screen_name, page_count=1):
        api = self.tweepy_api
        return tweepy.Cursor(api.user_timeline,
                             tweet_mode='extended',
                             screen_name=screen_name,
                             trim_user=True,
                             exclude_replies=True,
                             include_rts=False).items(page_count)
