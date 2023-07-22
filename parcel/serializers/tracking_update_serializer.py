from rest_framework import serializers

from parcel.models import TrackingUpdate


class TrackingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingUpdate
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
        }
