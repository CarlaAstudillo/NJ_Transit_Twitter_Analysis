#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
from datetime import timedelta

#Twitter API credentials
consumer_key = "eGWBnoJf21014qWJMObiS9WAC"
consumer_secret = "GPGgqls9yMFXSITtl9gOJfYqmI2X1r5Wqd5lKpfahKNkVR4cnP"
access_key = "205486955-vLiIYf69BGiQv4P5WpB2PaoHOUz36UHehD6rcZnY"
access_secret = "TRhZQ8chDfsJaFkPJzV1t9z2km2fWND7TRHdhWzsMXy5V"

tweetlink ="https://twitter.com/NJTRANSIT_MBPJ/status/"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
		
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at + timedelta(hours=-4), tweet.text.encode("utf-8"), tweetlink + str(tweet.id)] for tweet in alltweets]
	
	#write the csv	
	with open('csvs/%s_march_april_may.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "tweetlink"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("@NJTRANSIT_MBPJ")