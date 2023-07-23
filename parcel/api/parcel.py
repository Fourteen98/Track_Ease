from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from parcel.models import Parcel
from parcel.serializers import ParcelSerializer


class ParcelListCreateView(generics.ListCreateAPIView):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ParcelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_instance = serializer.save()
        parcel = ParcelSerializer(serializer_instance)
        return Response({"status": "success", "message": "Parcel Tracking Instantiated", "parcel": parcel.data},
                        status=status.HTTP_201_CREATED)

    def get(self, request, track_ease_id):
        res = {
            'is_error': False,
            'message': ''
        }
        try:
            parcel = Parcel.objects.get(id=track_ease_id)
            serializer = ParcelSerializer(parcel)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Parcel.DoesNotExist:
            res['is_error'] = True
            res['message'] = 'Parcel not found'
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, track_ease_id):
        res = {
            'is_error': False,
            'message': ''
        }
        try:
            parcel = Parcel.objects.get(pk=track_ease_id)
            serializer = ParcelSerializer(parcel, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            res['message'] = 'Parcel updated successfully'
            return Response(res, status=status.HTTP_200_OK)
        except Parcel.DoesNotExist:
            res['is_error'] = True
            res['message'] = 'Parcel not found'
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, track_ease_id):
        res = {
            'is_error': False,
            'message': ''
        }
        try:
            parcel = Parcel.objects.get(id=track_ease_id)
            serializer = ParcelSerializer(parcel, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            res['message'] = 'Parcel updated successfully'
            return Response(res, status=status.HTTP_200_OK)
        except Parcel.DoesNotExist:
            res['is_error'] = True
            res['message'] = 'Parcel not found'
            return Response(res, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, track_ease_id):

        try:
            parcel = Parcel.objects.get(id=track_ease_id)
            parcel.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except Parcel.DoesNotExist:
            res = {
                'is_error': True,
                'message': 'Parcel not found'
            }
            return Response(res, status=status.HTTP_404_NOT_FOUND)
