import pytest
from django.conf import settings
from django.contrib.auth.models import User, Group
from django.test import Client
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
        "longitude": fake.longitude(),
        "latitude": fake.latitude(),
        "address": fake.address(),
    }
    tracking_update = TrackingUpdate.objects.create(**defaults)
    return tracking_update


@pytest.fixture
@pytest.mark.django_db
def tracking_update_data(create_parcel_record):
    data = {
        "parcel": create_parcel_record.id,
        "longitude": fake.longitude(),
        "latitude": fake.latitude(),
        "address": fake.address(),
    }
    return data


@pytest.fixture
@pytest.mark.django_db
def login_user(**kwargs):
    # create a current user for testing
    def _login_user(group=kwargs.get("group", None)):
        username = 'admin'
        password = 'admin'
        client = Client()
        user = User.objects.create_user(username=username, password=password)
        client.login(username=username, password=password)
        return user, client

    return _login_user


@pytest.fixture
def django_admin_user_client(client):
    # Create a superuser for Django admin
    user = User.objects.create_superuser(
        username='admin',
        password='admin',
        email='admin@example.com'
    )

    # Log in the superuser client
    client.login(username='admin', password='admin')

    return client


@pytest.fixture
def create_group():
    def _create_group(name):
        return Group.objects.create(name=name)

    return _create_group


@pytest.fixture
def create_user_with_group():
    def _create_user_with_group(username, password, email, group_name):
        user = User.objects.create_user(username=username, password=password, email=email)
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        return user

    return _create_user_with_group
