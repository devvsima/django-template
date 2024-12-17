# from rest_framework import serializers

# from .models import Projects

# class UsersModel:
#     def __init__(self, id, username, language):
#         self.id = id
#         self.username = username
#         self.language = language

from rest_framework import serializers
from .models import TgUsers

class TgUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUsers
        fields = '__all__'

# class UsersSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     username = serializers.CharField()
#     language = serializers.CharField()