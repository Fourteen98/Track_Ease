from parcel.gmaps.geocoding import Geocoding


class TestGeocoding:
    def test_geocoding(self):
        geocoding = Geocoding()
        assert geocoding.geocode("1600 Amphitheatre Parkway, Mountain View, CA") == {'lat': 37.4223878,
                                                                                     'lng': -122.0841877}, "Should " \
                                                                                                           "return " \
                                                                                                           "the " \
                                                                                                           "coordinates"

    def test_geocoding_invalid_address(self):
        geocoding = Geocoding()
        assert geocoding.geocode("invalid address") == {}, "Should return an empty dictionary"

    def test_geocoding_empty_address(self):
        geocoding = Geocoding()
        assert geocoding.geocode("") == {}, "Should return an empty dictionary"

    def test_reverse_geocoding(self):
        geocoding = Geocoding()
        assert isinstance(geocoding.reverse_geocode(6.063632961177632, -0.2608496918918269), str), "Should return the " \
                                                                                                   "address"
