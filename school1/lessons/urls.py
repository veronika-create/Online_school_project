from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('Lessons_all/', views.index, name='index'),
    path('<slug:lessons_slug>/', views.LessonsDetailView.as_view(), name='Lessons_all'),
    path('Profile_std/', views.Profile_std, name='Profile_std')

]