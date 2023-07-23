from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

ROOT_URl = ""


class SwaggerTrackEasySchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    config = {
        "title": "Track Ease API",
        "description": "TrackEase is a Django-based web application that allows users to track their parcels in "
                       "real-time. The service provides live updates on the status and location of parcels as they "
                       "are being delivered, ensuring users have accurate information at their fingertips",
        "url": ROOT_URl,
        "patterns": [
            path('parcel/', include('parcel.urls')),
            path('accounts/', include('django.contrib.auth.urls')),
        ]
    }

    def get(self, request):
        generator = SchemaGenerator(**self.config)
        schema = generator.get_schema(request=request, public=True)
        return Response(schema)
