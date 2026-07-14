from django.contrib import admin


from groups.models import Courses
from groups.models import Groups, Teachers_сourses, Teachrs_groups






@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Teachers_сourses)
class Teachers_сoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Teachrs_groups)
class Teachrs_groupsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}




