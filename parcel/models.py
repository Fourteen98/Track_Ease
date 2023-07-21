from django.db import models
import uuid


class Parcel(models.Model):
    tracking_number = models.CharField(max_length=50, unique=True)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    current_status = models.CharField(max_length=50)
    delivery_address = models.CharField(max_length=200)

    def __str__(self):
        return self.tracking_number
