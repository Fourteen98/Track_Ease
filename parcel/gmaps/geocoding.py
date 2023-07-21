import googlemaps


class Geocoding(object):
    def __init__(self, api_key):
        self.client = googlemaps.Client(key=api_key)

    def geocode(self, address):
        pass
