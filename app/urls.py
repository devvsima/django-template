from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('main.urls', namespace='main')),
    path('user/', include('users.urls', namespace='user')),
    
]
from .settings import DEBUG
if DEBUG:
    from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
