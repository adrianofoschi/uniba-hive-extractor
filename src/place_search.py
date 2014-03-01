# Import the relevant libraries
from urllib.request import urlopen
import json
import sys

# @input LOCATION
LOCATION = sys.argv[1]

# Define the radius (in meters)
RADIUS = 30

# Set the Places API key
AUTH_KEY = "..."

# Create and send the request
endpoint = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
         'location=%s&radius=%s&sensor=false&key=%s') % (LOCATION, RADIUS, AUTH_KEY)
response = urlopen(endpoint)

# Get the response and use the JSON library to decode the JSON
json_raw = response.read().decode('utf8')
places = json.loads(json_raw)

# Print the places
for place in places['results']:
	print(json.dumps(place))