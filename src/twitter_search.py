# Import the relevant libraries
import oauth2 as oauth
import json
import sys

# @input LOCATION
LOCATION = sys.argv[1]

# Define the radius (in kilometers)
RADIUS = 0.1

# Set the Twitter oauth2 API keys
CONSUMER_KEY = "mlqhb4ULVk1wvfvU4gGyXA"
CONSUMER_SECRET = "aXv2iiYm9OKoLPdZLKHIh8QiixbmdfSsUiTL7KzAV0"
ACCESS_KEY = "2203839993-KsWpfy9RS0JScT2QsCLtDECxTkqiacG1h3VHrcF"
ACCESS_SECRET = "X4zHaHQlwoT9nzy3DlIXiQSiuHfFhvYZVV2E6VEfWEdI7"

# Create oauth2 token
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)

# Instantiate the client
client = oauth.Client(consumer, access_token)

# Create and send the request
endpoint = ('https://api.twitter.com/1.1/search/tweets.json'
	'?&geocode=%s,%skm') % (LOCATION, RADIUS)
response, data = client.request(endpoint)

# Get the response and use the JSON library to decode the JSON
tweets = json.loads(data)

# Print the statuses
for status in tweets['statuses']:
	print json.dumps(status)