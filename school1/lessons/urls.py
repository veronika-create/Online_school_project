from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('lessons_all/', views.index, name='index'),
    path('<slug:lessons_slug>/', views.lessons_all, name='lessons_all'),
    path('Profile_std/', views.Profile_std, name='Profile_std')

]

#path('<slug:lessons_slug>/', views.LessonsDetailView.as_view(), name='lessons_all'),