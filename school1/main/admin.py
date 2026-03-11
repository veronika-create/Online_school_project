from django.contrib import admin

from main.models import Categories
from main.models import Subjects
from main.models import About_us
from main.models import Teachers 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(About_us)
class About_usAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Teachers )
class TeachersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



