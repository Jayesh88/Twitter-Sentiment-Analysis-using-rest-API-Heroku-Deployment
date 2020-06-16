# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:45:04 2020

@author: HP PC
"""

from flask import Flask, request, render_template
import Twitter_Sentiment_Analysis


app = Flask(__name__)



@app.route('/')
def home(): 
    return render_template('Twitter.html')


@app.route('/keyword',methods=['POST','GET'])
def keyword():
    #val = request.form.get("val")
    val=request.form["keyword"]
    word=Twitter_Sentiment_Analysis.keyword.key(val)
    polarity=Twitter_Sentiment_Analysis.plotting.PolarityAndSubjectivity(word)
        
    word_cld=Twitter_Sentiment_Analysis.plotting.show_wordcloud(word['tweets'])
    negative_positive_plot=Twitter_Sentiment_Analysis.plotting.sentiment(word)
    
    return render_template('Twitter.html',prediction=word['tweets'].head(),Top_Five_Tweets="Top Five Raw Tweets:",plot=word_cld,Word_cloud="Word Cloud for common words used in the Tweets",plot_polarity=polarity,polatiry_plot="Relationship between Subjectivity and Polarity",plot_sentiment=negative_positive_plot,Sentiment="Count of Positive, Negative and Neutral Tweets")
    


if __name__ == "__main__":
    app.run()
    
