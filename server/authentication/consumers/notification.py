import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer


class NewUserConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'new_user'
        self.room_group_name = 'notification'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': 'new_user_notification',
                'message': json.loads(text_data)['message']
            }
        )

    def new_user_notification(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'new_user'
        }))

    def user_online(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message,
            'status': 'status_change'
        }))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
