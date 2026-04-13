from django.contrib import admin

from lessons.models import Lessons


#admin.site.register(Lessons)


@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

