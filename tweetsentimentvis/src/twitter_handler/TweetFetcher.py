#! /usr/bin/env python

### this is the main code for Twitter Handler component


import tweepy
import datetime

from tweetsentimentvis.models import TweetObject

def fetch(q):
      ''' input a query q, this will fetch 100 recent tweets from the twitter server '''

      auth = tweepy.OAuthHandler('Ohqs1xx5t6XOfm1Fm7qHeVfz2','zLWvNpBLPIbPhSyawX8PuN9wDkB8OEv1fLt8IlOmib7ZqwPkiQ')
      auth.set_access_token('2489682726-hOGLydWvgQn79GmXl0BmjnVCYGtmNmI5CFF7HEb','adQzxcB7S0EE3j62JCZRqf0l6Iu9VPdAONcnOf7IUrFRX')
      api = tweepy.API(auth)


      raw_tweets = api.search(q,count=100)

      tweetlist = []
      all_objects = TweetObject.objects.all()
      all_objects.delete()

      for raw_tweet in raw_tweets:
            if raw_tweet.lang == "en":
                    new_tweet = TweetObject()
                    new_tweet.text = raw_tweet.text
                    new_tweet.user = raw_tweet.user.name
                    new_tweet.date = raw_tweet.created_at
                    new_tweet.save()
                    tweetlist.append(new_tweet)

      return tweetlist







