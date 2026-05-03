from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('lessons_all/', views.lessons, name='lessons'),
    path('lessons_all/<slug:lessons_slug>/', views.lessons_all, name='lessons_all'),
    
    

]

#path('<slug:lessons_slug>/', views.LessonsDetailView.as_view(), name='lessons_all'),