from django.contrib import admin

# Register your models here.
from .models import Categories, Tags, Projects, ProjectImage

admin.site.register([Categories, Tags, Projects, ProjectImage])
