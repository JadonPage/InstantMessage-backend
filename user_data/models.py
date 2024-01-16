from django.db import models


class UserData(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    can_create_account = models.BooleanField(null=False, default=False)
    authenticated = models.BooleanField(null=False, default=False)
    can_create_chat = models.BooleanField(null=False, default=False)
    friend_search = models.CharField(max_length=20)
    message_to_send = models.CharField(max_length=500)
    time_sent = models.DateTimeField(auto_now_add=True)
    time_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.username}"


