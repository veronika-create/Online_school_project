

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from school import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('lessons/', include('lessons.urls', namespace='lessons_all')),
    path('user/', include('users.urls', namespace='user')),
    #path('prep/', include('groups.urls', namespace='groups')),
    path('subjects_all/', include('main.urls', namespace='subjects_all')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('questions/', include('testing.urls', namespace='questions')),
	#path('testapi/', views.QuizApiList.as_view()),
    #path('accounts/', include('users.urls', namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns +=[
        path("__debug__/", include("debug_toolbar.urls")),
    
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


