# Import the relevant libraries
from requests_oauthlib import OAuth1Session
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

# Create and send the request
twitter = OAuth1Session(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
url = ('https://api.twitter.com/1.1/search/tweets.json?'
         '&geocode=%s,%skm') % (LOCATION, RADIUS)
r = twitter.get(url)

# Get the response and use the JSON library to decode the JSON
tweets = json.loads(r.text)

# Print the statuses
for status in tweets['statuses']:
	print(json.dumps(status))