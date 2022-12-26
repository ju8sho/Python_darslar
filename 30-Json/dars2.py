"""
SUSAMBIL



"""

import json
import googlemaps
from apikey import APIKEY

#Googlemaps
gmaps = googlemaps.Client(key=APIKEY)

data = gmaps.geocode('Pop, Namangan')

g = json.dumps(data[0], index = 4, sort_keys=True)
