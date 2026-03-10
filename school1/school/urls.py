from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('std/', include('lessons.urls', namespace='lessons')),
    path('adm/', include('users.urls', namespace='users')),
    path('prep/', include('groups.urls', namespace='groups')),
]


