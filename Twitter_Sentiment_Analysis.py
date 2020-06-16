# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:35:30 2020

@author: HP PC
"""
from tweepy import API 
from tweepy import OAuthHandler
from io import BytesIO
import base64

from textblob import TextBlob
 
import Twitter_credentials

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import re


class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(Twitter_credentials.CONSUMER_KEY, Twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(Twitter_credentials.ACCESS_TOKEN, Twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth
    
    
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client



class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweets_to_data_frame(self, tweets):  
        df = pd.DataFrame([tweet.full_text for tweet in tweets], columns=['tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.full_text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['sentiment'] = np.array([self.analyze_sentiment(tweet) for tweet in df['tweets']])
        df['polarity']=np.array([self.Polarity(tweet) for tweet in df['tweets']])
        df['subjectivity']=np.array([self.subjectivity(tweet) for tweet in df['tweets']])
        return df

    def Polarity(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        polarity = analysis.sentiment.polarity 
        return polarity
        
    
    def subjectivity(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        subjectivity = analysis.sentiment.subjectivity
        return subjectivity
    

    
class keyword():
    def key(word):
        twitter_client = TwitterClient()
        tweet_analyzer = TweetAnalyzer()
    
        api = twitter_client.get_twitter_client_api()
    
        tweets = api.user_timeline(screen_name=word, count=200, tweet_mode='extended')
    
        df = tweet_analyzer.tweets_to_data_frame(tweets)
        return df



class plotting():
    def show_wordcloud(data, title = None):
        img = BytesIO()
        stopwords = set(STOPWORDS)
        wd = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
        ).generate(str(data))
    
        
        plt.axis('off')
        #plt.figure(0)
        plt.imshow(wd,interpolation='bilinear')
        wd.to_image().save(img, 'JPEG')
        #plt.show()
        img.seek(0)
        plotwrd = base64.b64encode(img.getvalue())
        plt.close()
        return plotwrd.decode('utf-8')
    
    def sentiment(wrd):
        #df=self.tweets_to_data_frame()
        data=[]
        for sent in range(0,len(wrd)):
            if wrd['sentiment'][sent]>0:
                strng='Positive'
                data.append(strng)
            elif wrd['sentiment'][sent]==0:
                strng='Neutral'
                data.append(strng)
            else:
                strng='Negative'
                data.append(strng)
        dd=pd.DataFrame(data,columns=["sentiments"])
        sns.catplot(x="sentiments", kind="count", palette="Blues_d", data=dd)
        #plt.figure(1)
        img = BytesIO()
        plt.savefig(img, format='png')
        #plt.show()
        img.seek(0) 
        plotsenti = base64.b64encode(img.getvalue())
        plt.close()
        return plotsenti.decode('utf-8')
        

    def PolarityAndSubjectivity(df):
        
        plt.rcParams['figure.figsize'] = [10, 8]
        
        for index, tweets in enumerate(df.index):
            x = df.polarity.loc[tweets]
            y = df.subjectivity.loc[tweets]
            plt.scatter(x, y, color='Red')
            plt.title('Sentiment Analysis', fontsize = 20)
            plt.xlabel('Polarity', fontsize=15)
            plt.ylabel('Subjectivity', fontsize=10)
        #plt.figure(2)
        img2 = BytesIO()
        plt.tight_layout()
        plt.savefig(img2, format='jpeg',dpi=500)
        img2.seek(0)
        plot_url = base64.b64encode(img2.getvalue())
        
        return plot_url.decode('utf-8')

        
#for testing purpose
if __name__ == '__main__':
    
    wrd=keyword.key("who")
    cld=plotting.show_wordcloud(wrd['tweets'])
    plotting.sentiment(wrd)
    #plt.close()
    plotting.PolarityAndSubjectivity(wrd)
    
    

