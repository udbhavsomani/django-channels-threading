from channels.routing import ProtocolTypeRouter, URLRouter
import os

from django.core.asgi import get_asgi_application
from django.urls import path

import home.consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()

ws_patterns = [
    path('ws/', home.consumers.DataConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})
