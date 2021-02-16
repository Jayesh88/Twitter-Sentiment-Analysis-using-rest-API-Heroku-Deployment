# Twitter Sentiment Analysis using rest API-Heroku Deployment

## Prerequisits required:
1. Need a twitter account
2. Create an app https://developer.twitter.com/en/apps, from where you can generate credentials like ACCESS_TOKEN,ACCESS_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET


## Project is divided into 3 parts:

1. Twitter_credentials.py- As mentioned in pre-requisits you need to create an app @twitter development to get the necessary credentials for execution of this file.

2. Twitter_sentiment_analysis.py- 
      - This py file uses OAuth API to fetch tweets from live twitter application.
      - Used TextBlob one o the concepts of NLP for checking subjectivity and polarity of tweets.
      - Created Scatter Plot using library seaborn to visualize the relationship between "Subjectivity" and "Polarity" of tweets.
      - Created Bar graph using library matplotlib to check the imapct of tweets whether it is positive, negative or Neutral.
      - Built a word chart using library wordcloud to visualize most common words.
      
3. Twitter_app.py- This py file will create an API, using library flask , this will basically accept inputs from the user at runtime and generate an output from Twitter_sentiment_analysis.py.


## Deployment In Heroku:
You just have to create an account in Heroku, connect your github repository with it that you wish to create a server for.

Create two additional things before you deploy in heroku-
 - Create a procfile which you can view in this repository , in which you will need to add your app name which in my case it is Twitter_app and the other thing is you need to specify the name of flask object that you have created. In my case, For example: Twitter_app : app, my "app" is the flask object which is created.
 - Requiremnts file where you have to specify all the libraries that you have imported , along with its versions. The same can be found in this repository. If you want to know the version installed in your ,machine of differnt libraries, open your anaconda prompt and just type.
 
            
            pip Freeze

This project can be viewed at https://twittersentimentanalysis-app.herokuapp.com/

