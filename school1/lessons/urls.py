from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us_std/', views.about_us_std, name='about_us_std'),

]