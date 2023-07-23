import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class TrackingConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.group_name = None
        self.user = None
        self.track_ease_id = None

    def connect(self):
        # should get the track_ease_id from the url
        self.track_ease_id = self.scope["url_route"]["kwargs"]["track_ease_id"]
        # should get the current login user from the request object
        self.user = self.scope["user"]
        # check if the user group is dispatch
        if self.user.groups.filter(name="dispatch").exists():
            # create a group name for the track_ease_id
            self.group_name = f"tracking_{self.track_ease_id}"
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            self.accept()
        elif self.user.groups.filter(name="recipient").exists():
            self.group_name = f"tracking_{self.track_ease_id}"
            # check if room exists
            if not self.channel_layer.group_channels(self.group_name):
                self.close()
            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            self.accept()

        else:
            self.close()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        if 'location' in data:
            pass
