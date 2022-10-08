import tweepy
import os 
from textblob import TextBlob
#commented by lesia
#Authenticate to twitter
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")

    listOfTweets = []

    #search for tweet query 
    for tweet in api.search(q="la croix", lang="en", rpp=10):
        t = f"{tweet.text}"

        if ":" in t:
            colon = t.index(":")
            t = t[colon + 1:]
        listOfTweets.append(t)

    num = 1
    score = 0
    count = len(listOfTweets)

    for tweet in listOfTweets:
        print(num, tweet)
        num += 1
        text = TextBlob(tweet)
        print(text.sentiment.polarity)
        score += text.sentiment.polarity
        print("---------------------------")
    print("Average Sentiment Polarity on current topic is:", score/count)

except:
    print("Error during authentication")
