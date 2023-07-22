from django.conf import settings
from django.urls import path

from parcel.api.parcel import ParcelListCreateView
from parcel.swagger.swagger_schema import SwaggerTrackEasySchemaView

app_name = 'parcel'
api_version = "api/v1"

urlpatterns = [
    # Views URL
    path(f'{api_version}/track-ease/<str:track_ease_id>', ParcelListCreateView.as_view(), name='track_ease'),
]

if settings.DEBUG:
    urlpatterns.append(path(f'{api_version}/docs/', SwaggerTrackEasySchemaView.as_view()))
