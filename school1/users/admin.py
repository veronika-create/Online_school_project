from django.contrib import admin

from users.models import Registed_users
from users.models import List_of_students 
from users.models import List_of_teachers_for_goups
from users.models import List_of_teachers

@admin.register(Registed_users)
class Registed_usersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(List_of_students )
class List_of_studentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(List_of_teachers_for_goups)
class List_of_teachers_for_goupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(List_of_teachers)
class List_of_teachersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

