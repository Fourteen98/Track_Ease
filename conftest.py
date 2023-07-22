import pytest
from faker import Faker

from parcel.models import Parcel, TrackingUpdate

fake = Faker()


@pytest.fixture
@pytest.mark.django_db
def create_parcel_record():
    defaults = {
        "tracking_number": fake.random_int(),
        "departure_address": fake.address(),
        "destination_address": fake.address(),
        "current_status": fake.word(),
    }
    parcel = Parcel.objects.create(**defaults)
    return parcel


@pytest.fixture
@pytest.mark.django_db
def parcel_data():
    data = {
        "tracking_number": fake.random_int(),
        "departure_address": fake.address(),
        "destination_address": fake.address(),
        "current_status": fake.word(),
    }
    return data


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


@pytest.fixture
@pytest.mark.django_db
def tracking_update_data(create_parcel_record):
    data = {
        "parcel": create_parcel_record.id,
        "location": fake.address(),
        "status": 'pending',
        "notes": fake.text(),
    }
    return data
