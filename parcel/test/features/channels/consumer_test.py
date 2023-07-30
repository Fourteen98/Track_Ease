import json
from channels.testing import WebsocketCommunicator
from django.test import TestCase
from django.contrib.auth.models import User, Group

from parcel.models import TrackingUpdate
from parcel.channels.consumers import TrackingConsumer  # Replace 'myapp' with your actual app name


class TrackingConsumerTestCase(TestCase):
    def setUp(self):
        self.group_dispatch = Group.objects.create(name='dispatch')
        self.group_recipient = Group.objects.create(name='recipient')
        self.user_dispatch = User.objects.create_user(username='dispatch_user', password='password')
        self.user_dispatch.groups.add(self.group_dispatch)
        self.user_recipient = User.objects.create_user(username='recipient_user', password='password')
        self.user_recipient.groups.add(self.group_recipient)
        self.track_ease_id = 'sample_track_ease_id'
        self.communicator_dispatch = WebsocketCommunicator(
            TrackingConsumer.as_asgi(), f'/tracking/{self.track_ease_id}/?token={self.user_dispatch.auth_token}'
        )
        self.communicator_recipient = WebsocketCommunicator(
            TrackingConsumer.as_asgi(), f'/tracking/{self.track_ease_id}/?token={self.user_recipient.auth_token}'
        )

    async def test_dispatch_user_connect(self):
        connected, _ = await self.communicator_dispatch.connect()
        self.assertTrue(connected)
        # Write further tests based on your requirements for dispatch users.

    async def test_recipient_user_connect(self):
        connected, _ = await self.communicator_recipient.connect()
        self.assertTrue(connected)
        # Write further tests based on your requirements for recipient users.

    async def test_unauthenticated_user_connect(self):
        communicator = WebsocketCommunicator(
            TrackingConsumer.as_asgi(), f'/tracking/{self.track_ease_id}/?token=invalid_token'
        )
        connected, _ = await communicator.connect()
        self.assertFalse(connected)
        # Write further tests based on your requirements for unauthenticated users.

    async def test_receive_and_disconnect(self):
        await self.communicator_dispatch.connect()
        message = {
            'location': {
                'latitude': 123.456,
                'longitude': 456.789,
            }
        }
        await self.communicator_dispatch.send_json_to(message)
        response = await self.communicator_dispatch.receive_json_from()
        self.assertEqual(response['latitude'], 123.456)
        self.assertEqual(response['longitude'], 456.789)
        self.assertTrue(await self.communicator_dispatch.disconnect())
        # Write further tests for receiving messages and disconnection scenarios.

    def test_create_tracking_update(self):
        count_before = TrackingUpdate.objects.count()
        TrackingUpdate.objects.create(parcel_id=self.track_ease_id, longitude=0, latitude=0, address='Test Address')
        count_after = TrackingUpdate.objects.count()
        self.assertEqual(count_after, count_before + 1)
        # Write further tests for the creation of TrackingUpdate objects.
