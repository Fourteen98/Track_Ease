from dotenv import load_dotenv
import os
import googlemaps

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
