from TwitterSearch import *
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

def HashTracker():
 #ts = TwitterSearch(
          #consumer_key = 'oiqPmaj6hTVywkKlizDzw50l8',
          #consumer_secret = 'jHSBDW8E1doOnKKfabdMEnJFIIU0UCz9ufVwvhNhlDNu0Hessq',
          #access_token = 'boomgoes',
          #access_token_secret = 'thedynamite')
    try:
        
        tso = TwitterSearchOrder()
        tso.set_keywords(["#lol"])
        tso.set_negative_attitude_filter()
        tso1 = TwitterSearchOrder()
        tso1.set_keywords(["#lol"])
        tso1.set_positive_attitude_filter()

        ts = TwitterSearch(
            consumer_key = 'oiqPmaj6hTVywkKIizDzw50l8',
            consumer_secret = 'jHSBDW8E1doOnKKfabdMEnJFIIU0UCz9ufVwvhNhIDNu0Hessq',
            access_token = '42780587-4kuFLgjRn0sq4EyE1hUqdsXhkPRMt0SwvFfHsv3Dr',
            access_token_secret = 'MuljzOQYyOyaI4A0098vVDZc6xTcBeCfRSi0iUbYDMrDc')

        neg = 0
        pos = 0

        for tweet in ts.search_tweets_iterable(tso):
            
            neg = neg+1
        print(neg)


        for tweet in ts.search_tweets_iterable(tso1):

            pos = pos+1
        print(pos)

    except TwitterSearchException as e:
        print(e)
        
HashTracker()
