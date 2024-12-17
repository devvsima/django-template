from django.db import models
from datetime import datetime

# Create your models here.
class TgUsers(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, verbose_name="ID пользователя Telegram")
    username = models.CharField(max_length=200, verbose_name="Имя пользователя")
    language = models.CharField(max_length=10, verbose_name="Язык")
    role = models.CharField(max_length=10, verbose_name="Роль")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tg_users"
        verbose_name = "тг пользователь"
        verbose_name_plural = "тг пользователи"

    def __str__(self) -> str:
        return self.username