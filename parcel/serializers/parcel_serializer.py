from rest_framework import serializers

from parcel.models import Parcel


class ParcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcel
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
        }
