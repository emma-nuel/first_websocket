import json
from channels.generic.websocket import AsyncWebsocketConsumer
#from .models import LocationData
#from asgiref.sync import sync_to_async

class TrackerConsumer(AsyncWebsocketConsumer):
        
    async def connect(self):
        await self.accept()
        print('WebSocket connected')
        
    async def disconnect(self, close_code):
        print('WebSocket disconnected')
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        print('Received data from ESP32:', data)

        if 'lat' in data:
            print(data['lat'])
        else:
            print("Content does not exist")


