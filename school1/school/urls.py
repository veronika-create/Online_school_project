

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from school import settings
#from school import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('Lessons_all/', include('lessons.urls', namespace='lessons')),
    path('adm/', include('users.urls', namespace='users')),
    path('prep/', include('groups.urls', namespace='groups')),
    path('Subjects_all/', include('main.urls', namespace='Subjects_all')),
]

if settings.DEBUG:
    urlpatterns +=[
        path("__debug__/", include("debug_toolbar.urls")),
    
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


