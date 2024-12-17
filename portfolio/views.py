from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
from rest_framework import generics

from .models import Projects, ProjectImage
from .serializers import PortfolioSerializer

class PortfolioAPIView(generics.ListAPIView):
    queryset =  Projects.objects.all()
    serializer_class = PortfolioSerializer


from .models import Projects
def catalog(request) -> HttpResponse:
    data = Projects.objects.all()
    context = {
        "title": 'Name',
        "projects": data
    }
    return render(request, 'catalog/catalog.html', context)

def project(request, project_id):
    data = Projects.objects.get(id=project_id)
    images = ProjectImage.objects.filter(project=project_id)
    print(images)
    context = {
        "title": 'Name',
        "project": data,
        "images": images
    }
    return render(request, "project/project.html", context)