from django.contrib import admin


from groups.models import Courses
from groups.models import Groups






@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}




