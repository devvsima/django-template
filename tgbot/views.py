from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import TgUsers
from .serializers import TgUsersSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

class TgUsersListCreateView(generics.ListCreateAPIView):
    queryset = TgUsers.objects.all()
    serializer_class = TgUsersSerializer
    
    @action(detail=True, methods=['patch'])
    def change_language(self, request, pk=None):
        """Изменение языка пользователя"""
        user = self.get_object()  # Получаем пользователя по ID
        new_language = request.data.get('language')
        if not new_language:
            return Response({"error": "Language not provided"}, status=status.HTTP_400_BAD_REQUEST)
        user.language = new_language
        user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)