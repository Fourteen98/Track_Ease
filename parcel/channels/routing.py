from django.urls import path

from parcel.channels.consumers import TrackingConsumer

websocket_urlpatterns = [
    path('ws/tracking/', TrackingConsumer.as_asgi(), name='tracking'),
]
