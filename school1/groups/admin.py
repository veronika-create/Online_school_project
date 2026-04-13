from django.contrib import admin


from groups.models import Courses
from groups.models import Groups
from groups.models import Material_for_students
from groups.models import Base_of_knowledge
from groups.models import Lectures



@admin.register(Lectures)
class LecturesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Base_of_knowledge)
class Base_of_knowledgeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Material_for_students)
class Material_for_studentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



