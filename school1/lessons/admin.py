from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from lessons.models import Lessons


#admin.site.register(Lessons)


@admin.register(Lessons)
class LessonsAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass