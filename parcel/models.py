from django.db import models
from parcel.base import BaseModel
import uuid

COMPLETED = "completed"
PENDING = "pending"

COMPLETION_STATUS = (
    (PENDING, PENDING),
    (COMPLETED, COMPLETED),
)


class Parcel(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tracking_number = models.CharField(max_length=50, unique=True)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    current_status = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=200)
    completion_status = models.CharField(max_length=200, default=PENDING, choices=COMPLETION_STATUS)

    def __str__(self):
        return self.tracking_number
