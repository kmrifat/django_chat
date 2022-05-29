from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from chat_app.authentication import BearerAuthentication
from chat_app.serializers import UserSerializer


class StartCallSerializer(serializers.Serializer):
    receiver = serializers.SlugField()
    sender = serializers.SlugField()
    peer_id = serializers.CharField()


class StartCall(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = StartCallSerializer(data=request.data)
        if serializer.is_valid():
            sender_user = User.objects.get(username=serializer.validated_data['sender'])
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'chat_%s' % serializer.validated_data['receiver'], {
                    'type': 'new_call',
                    'message': {
                        'data': serializer.validated_data,
                        'display': UserSerializer(sender_user, context={'request': request}).data
                    }
                }
            )
            print('all good')
            return Response({'hello': 'world'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JoinCallSerializer(serializers.Serializer):
    peer_js = serializers.CharField()


class EndCall(APIView):
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = StartCallSerializer(data=request.data)
        if serializer.is_valid():
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'chat_%s' % serializer.validated_data['peer_id'], {
                    'type': 'end_call',
                    'message': {
                        'data': serializer.validated_data,
                    }
                }
            )
            return Response({'hello': 'world'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
