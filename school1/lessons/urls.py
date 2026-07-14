from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('lessons_all/', views.lessons, name='lessons'),
    path('lessons_all/<slug:lessons_slug>/', views.lessons_all, name='lessons_all'),
    path('Plan/', views.Plan_list, name='Plan'),
    path('Marks/', views.Marks_list, name='Marks'),
    path('homework/', views.homework_list, name='homework'),
    path('stud_marks/', views.stud_marks_list, name='stud_marks'),
    path('table/', views.table_list , name='table'),
    path('library/', views.Library_list, name='library'),
    
    

]

#path('<slug:lessons_slug>/', views.LessonsDetailView.as_view(), name='lessons_all'),