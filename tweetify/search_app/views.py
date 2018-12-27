from django.shortcuts import render
from search_app.forms import SearchForm
import tweepy
from textblob import TextBlob
import os
import random

from search_app.forms import SearchForm

def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print("Topic is",search)

            consumer = os.environ.get('consumer')
            consumer_secret = os.environ.get('consumer_secret')

            access_token = os.environ.get('access_token')
            access_token_secret = os.environ.get('access_token_secret')

            auth = tweepy.OAuthHandler(consumer,consumer_secret)
            auth.set_access_token(access_token,access_token_secret)
            api = tweepy.API(auth)

            tweets = api.search(q=search,count=5000,tweet_mode='extended',lang='en')
            sentiment_list = []
            for tweet in tweets:
                blob = TextBlob(tweet.full_text)
                sentiment = blob.sentiment.polarity
                sentiment_list.append(sentiment)
    
            result = zip(tweets,sentiment_list)    
            return render(request,"search_app/list.html",{'result':result})

    value = random.randint(0,30)
    value2 = random.randint(0,30)

    with open(os.path.dirname(os.path.realpath(__file__)) + '\quotes.txt','r') as f:
        for  i,line in enumerate(f):
            if i==value:
                myline = line
            if i==value2:
                myline2 = line    
                
    line_comp = myline.split('-')
    quote = line_comp[0]
    source = line_comp[1]

    line_comp2 = myline2.split('-')
    quote2 = line_comp2[0]
    source2 = line_comp2[1]
         

    return render(request,"search_app/index.html",{'form':form,'quote':quote,'source':source,'quote2':quote2,'source2':source2})
