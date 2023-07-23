from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from parcel.models import Parcel, TrackingUpdate
from parcel.serializers import TrackingUpdateSerializer


class TrackingUpdateListCreateView(generics.ListCreateAPIView):
    queryset = TrackingUpdate.objects.all()
    serializer_class = TrackingUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, track_ease_id):
        res = {
            'is_error': False,
            'message': ''
        }
        try:
            Parcel.objects.get(id=track_ease_id)
            serializer = TrackingUpdateSerializer(data=request.data)
            if serializer.is_valid():
                tracking_update = serializer.save()
                tracking_update.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                res['is_error'] = True
                res['message'] = serializer.errors
                return Response(res, status=status.HTTP_400_BAD_REQUEST)
        except Parcel.DoesNotExist:
            res['is_error'] = True
            res['message'] = 'Parcel not found'
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, track_ease_id):
        res = {
            'is_error': False,
            'message': ''
        }
        try:
            parcel = Parcel.objects.get(id=track_ease_id)
            serializer = TrackingUpdateSerializer(parcel.updates.all(), many=True)
            if not serializer.data:
                res['is_error'] = True
                res['message'] = 'No tracking updates found'
                return Response(res, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Parcel.DoesNotExist:
            res['is_error'] = True
            res['message'] = 'Parcel not found'
            return Response(res, status=status.HTTP_404_NOT_FOUND)
