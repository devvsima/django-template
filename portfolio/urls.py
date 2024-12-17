from django.urls import path

from . import views

app_name = 'portfolio'

from .views import PortfolioAPIView

urlpatterns = [
    # path('api/', PortfolioAPIView.as_view()),
    path('catalog', views.catalog, name='catalog'),
    path('project/<slug:project_id>', views.project, name='project'),

]
