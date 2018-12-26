from django.shortcuts import render
from search_app.forms import SearchForm
import tweepy
from textblob import TextBlob

from search_app.forms import SearchForm

def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            print("Topic is",search)

            consumer = "NCp53tPqqk0cxBi8pS84osj1E"
            consumer_secret = "NWiaVLvmRlrUMiBOJWz17VU7w2xQKu3NpgpGkc6DCuiVcf64p6"

            access_token = "1072842454137589760-4o1HMJ4yauotAnmAY6rYvGlgOscqIQ"
            access_token_secret = "cvLthe84mu8fZdfms5CZMlqCGTUONHDGNIjG86FnnyeG1"

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

    return render(request,"search_app/index.html",{'form':form})
