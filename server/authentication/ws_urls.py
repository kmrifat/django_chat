from django.urls import path

from authentication import consumers

websocket_urlpatterns = [
    path('ws/notification/', consumers.NewUserConsumer.as_asgi()),
]
