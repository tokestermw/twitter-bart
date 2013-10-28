import tweepy
from tweepy import StreamListener
import json, time, sys


class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    def __init__(self):
        self.output  = open('./data/' + 'badabing' + '.'
                            + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        self.counter = 0


    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)
        self.output.write(status + "\n")

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])

        self.counter += 1
        if self.counter >= 180:
            self.output.close()
            return False

        return true

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
    listener = StdOutListener()

    consumer_key        = 
    consumer_secret     = 
    access_token        = 
    access_token_secret = 

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=['bartstrike'])
