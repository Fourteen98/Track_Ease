import os

import googlemaps
from dotenv import load_dotenv

load_dotenv()


class Geocoding(object):
    def __init__(self):
        self.client = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

    def geocode(self, address):
        if address:
            geocode_result = self.client.geocode(address)
            if geocode_result:
                return geocode_result[0]['geometry']['location']
        return {}

    def reverse_geocode(self, latitude, longitude):
        if latitude and longitude:
            reverse_geocode_result = self.client.reverse_geocode((latitude, longitude))
            if reverse_geocode_result:
                return reverse_geocode_result[0]['formatted_address']
        return ''
