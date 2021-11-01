# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # self.accept()
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]
        
        
        print("///" + self.scope["user"].username, end=" ///\n")
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # self.accept()

    async def disconnect(self, close_code):
        # pass
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        if self.scope["user"].username == " ":
            username = "Anonymous"
        else:
            username = self.scope["user"].username
        # username = self.scope["user"].username
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message = (username + " : " + message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
    
    # Receive message from room group
    async def chat_message(self, event):
        # username = self.scope["user"].username
        if self.scope["user"].username == " ":
            username = "Anonymous"
        else:
            username = self.scope["user"].username
        message = event['message']
        print(self.user.username)
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            "username": username,
        }))
