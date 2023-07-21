import pytest
from faker import Faker
from parcel.models import Parcel

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
        "completion_status": fake.word("pending", "completed"),
    }
    parcel = Parcel.objects.create(**defaults)
    return parcel
