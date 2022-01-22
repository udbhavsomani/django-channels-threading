import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'data_consumer'
        self.room_group_name = 'data_consumer_group'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(json.dumps({'status': 'connected to data consumer'}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.send(json.dumps({'message': f'Disconnected: {close_code}'}))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        await self.send(json.dumps({'status': 'Got the Data'}))

    async def send_data(self, event):
        data = json.loads(event['student_data'])
        await self.send(json.dumps({'payload': data}))
