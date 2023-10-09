import uuid

from django.db import models

from parcel.base import BaseModel

COMPLETED = "completed"
PENDING = "pending"

COMPLETION_STATUS = (
    (PENDING, PENDING),
    (COMPLETED, COMPLETED),
)


class Parcel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracking_number = models.CharField(max_length=50, unique=True)
    departure_address = models.CharField(max_length=200)
    destination_address = models.CharField(max_length=200)
    current_status = models.CharField(max_length=50)

    def __str__(self):
        return self.tracking_number


class TrackingUpdate(BaseModel):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE, related_name='updates')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.parcel.tracking_number} - {self.timestamp} - {self.latitude} - {self.longitude}"
