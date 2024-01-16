from rest_framework.serializers import ModelSerializer
from ..models import UserData


class UserDataSerializer(ModelSerializer):
    class Meta:
        model = UserData
        fields = ('username', 'password', 'can_create_account',
                  'authenticated', 'can_create_chat', 'friend_search',
                  'message_to_send', 'time_sent', 'time_received')
        read_only_fields = ('time_sent', 'time_received')


