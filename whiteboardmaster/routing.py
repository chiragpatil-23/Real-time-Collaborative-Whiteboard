from channels.routing import ProtocalTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from whiteboard.consumers import BoardConsumer

application = ProtocalTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        URLRouter([
            path('', BoardConsumer)
        ])
    )
})