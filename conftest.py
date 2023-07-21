import pytest
from faker import Faker

from parcel.models import Parcel, TrackingUpdate

fake = Faker()


@pytest.fixture
@pytest.mark.django_db
def create_parcel_record():
    defaults = {
        "tracking_number": fake.random_int(),
        "sender": fake.name(),
        "recipient": fake.name(),
        "current_status": fake.word(),
        "delivery_address": fake.address(),
    }
    parcel = Parcel.objects.create(**defaults)
    return parcel


@pytest.fixture
@pytest.mark.django_db
def create_tracking_update_record(create_parcel_record):
    defaults = {
        "parcel": create_parcel_record,
        "location": fake.address(),
        "status": fake.word(),
        "notes": fake.text(),
    }
    tracking_update = TrackingUpdate.objects.create(**defaults)
    return tracking_update
