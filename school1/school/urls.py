

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from school import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('lessons_all/', include('lessons.urls', namespace='lessons')),
    path('user/', include('users.urls', namespace='user')),
    path('prep/', include('groups.urls', namespace='groups')),
    path('subjects_all/', include('main.urls', namespace='subjects_all')),
    
    path('accounts/', include('users.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns +=[
        path("__debug__/", include("debug_toolbar.urls")),
    
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


