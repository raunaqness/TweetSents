
# coding: utf-8

# In[18]:

import tweepy
from textblob import TextBlob

import pandas as pd


# In[19]:

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""


# In[20]:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# In[21]:

api = tweepy.API(auth)


# In[81]:

tweet_data = {'Tweet': [],
        'Polarity': [],
        'Subjectivty': []}


# In[82]:

public_tweets = api.search('Hillary')

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    
    tweet_data["Tweet"].append(tweet.text)
    tweet_data["Polarity"].append(str(analysis.sentiment.polarity))
    tweet_data["Subjectivty"].append(str(analysis.sentiment.subjectivity))


# In[93]:

df = pd.DataFrame(tweet_data, columns = ['Tweet', 'Polarity', 'Subjectivty'])
df


# In[98]:

path = 'C:/Users/Raunaq/Desktop/Tweets_SentimentAnalysis.csv'
df.to_csv(path)

print("CSV file saved in " + path)

