from django.urls import path

from . import views

app_name = 'drf'

from portfolio.views import PortfolioAPIView
from tgbot.views import TgUsersListCreateView

urlpatterns = [
    path('portfolio/', PortfolioAPIView.as_view()),
    path('tgusers/', TgUsersListCreateView.as_view()),
]
