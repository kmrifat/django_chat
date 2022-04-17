from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404

from authentication.models import Profile


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    read = serializers.BooleanField()
    date_time = serializers.DateTimeField()
    sender_id = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    photo = serializers.ImageField(source='profile.photo')
    online = serializers.BooleanField(source='profile.online')
    status = serializers.CharField(source='profile.status')
    messages = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('name', 'username', 'photo', 'online', 'status', 'messages')

    def get_name(self, obj):
        if obj.first_name:
            return obj.get_full_name()
        return obj.username

    def get_messages(self, obj):
        return []


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = super(RegistrationSerializer, self).create(validated_data)
        self.__notify_others(user)
        return validated_data

    def __notify_others(self, user):
        serializer = UserSerializer(user, many=False)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'notification', {
                'type': 'new_user_notification',
                'message': serializer.data
            }
        )
