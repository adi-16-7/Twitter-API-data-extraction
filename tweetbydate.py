import tweepy
import datetime
consumerKey = "ib8ZI70KTBojgInsPcAY7un8k"
consumerSecret = "baVNbtiwPm8PQUj9K45sZLc3wqfU5UtrZk9m5vfAIUuhRA01TX"
accessToken = "315799226-KytKZHl4z7OMIkZCjgzZj06HChmucE66jRbzZcqz"
accessTokenSecret = "0HqxRat6weXKvKowrLabC25InBdLt4eUlOPDFCFjViUW7"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)



# auth = tweepy.AppAuthHandler(consumer_token, consumer_secret)
# auth.secure = True
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


api = tweepy.API(auth)

# username = "DelhiPolice"
startDate = datetime.datetime(2020, 3, 22, 0, 0, 0)
endDate =   datetime.datetime(2020, 3, 23, 0, 0, 0)


# query = 'DelhiPolice'
# max_tweets = 1000
# searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
# print(searched_tweets)
tweetsToSave=[]
tweets = api.search('@LtGovDelhi ', count=100000) #using @DelhiPolice, we'll get all tweets that have @DelhiPolice mentioned in them which includes the tweets by Delhi Police themselves
for i in tweets:
    if "RT @" not in i.text: #custom filter to filter out retweets
        if (str(i.user.name)=="LG Delhi" or str(i.user.location)=="28.6975° N, 77.2879° E, 1mi"): #filtering out the tweets by Delhi Police so that what we are left with is only mentions of @DelhiPolice
            # if str(i.user.location)=="28.6975° N, 77.2879° E":
            continue
        print(i.text , " " , i.created_at.strftime("%m/%d/%Y, %H:%M:%S") , " by ", i.user.name, "\n")
        tweetsToSave.append([i.text + " " + i.created_at.strftime("%m/%d/%Y, %H:%M:%S") + " by "+ i.user.name])
        # print(i.user.name+)
    # print()
# print(tweetsToSave)
import csv
# data_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
with open('tweets.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='|')
    writer.writerows(tweetsToSave) 
    print('Tweets Saved to tweets.csv successfully') 




# import tweepy
# import datetime
# consumerKey = "ib8ZI70KTBojgInsPcAY7un8k"
# consumerSecret = "baVNbtiwPm8PQUj9K45sZLc3wqfU5UtrZk9m5vfAIUuhRA01TX"
# accessToken = "315799226-KytKZHl4z7OMIkZCjgzZj06HChmucE66jRbzZcqz"
# accessTokenSecret = "0HqxRat6weXKvKowrLabC25InBdLt4eUlOPDFCFjViUW7"

# auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
# auth.set_access_token(accessToken, accessTokenSecret)



# # auth = tweepy.AppAuthHandler(consumer_token, consumer_secret)
# # auth.secure = True
# # api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# api = tweepy.API(auth)

# username = "DelhiPolice"
# startDate = datetime.datetime(2020, 3, 18, 0, 0, 0)
# endDate =   datetime.datetime(2020, 3, 21, 0, 0, 0)

# tweets = []
# tmpTweets = api.user_mentions(username)
# for tweet in tmpTweets:
#     if tweet.created_at < endDate and tweet.created_at > startDate:
#         tweets.append(tweet)

# while (tmpTweets[-1].created_at > startDate):
#     tmpTweets = api.user_mentions(username, max_id = tmpTweets[-1].id)
#     for tweet in tmpTweets:
#         if tweet.created_at < endDate and tweet.created_at > startDate:
#             tweets.append(tweet)

# for x in tweets:
# 	print(x.text + " " + x.created_at.strftime("%m/%d/%Y, %H:%M:%S") + "\n")