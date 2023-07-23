from rest_framework import serializers

from parcel.gmaps.geocoding import Geocoding
from parcel.models import TrackingUpdate


class TrackingUpdateSerializer(serializers.ModelSerializer):
    geocoding = Geocoding()

    class Meta:
        model = TrackingUpdate
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'address': {'read_only': True},
        }

    def create(self, validated_data):
        address = self.geocoding.reverse_geocode(validated_data['latitude'], validated_data['longitude'])
        validated_data['address'] = address
        return super().create(validated_data)
