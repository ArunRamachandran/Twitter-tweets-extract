import oauth2 as oauth
import json

CONSUMER_KEY = "cwUsz3slwPi9RuIP3U0hT5quQ"
CONSUMER_SECRET = "BgZd2QUevhcPjDXYzx87F3yFht7UYSNQqrFWwi76zZwM4HoH9p"
ACCESS_KEY = "3014167189-nhD1oedU6bFeLK41TGhKMvdapPSbfwjqzx2W72q"
ACCESS_SECRET = "i8ryrRgaf8RUPXSPBpuYegGESsgAjcYFKVk0wkxNaI9ix"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

def get_tweets(username, count):
	twt = []
	timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count="+count
	response, data = client.request(timeline_endpoint)

	tweets = json.loads(data)
	for tweet in tweets:
		twt.append(tweet['text'])
	return twt

username = raw_input('Give Username ?\n')
count = raw_input('No.of Tweets required ?\n')
tweets = get_tweets(username, count)
for tweet in tweets:
	print tweet,
	print "\n"
