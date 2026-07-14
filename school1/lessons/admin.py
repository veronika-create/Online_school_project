from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from lessons.models import Lessons, Teachers_paln, Marks, Library, table, stud_marks, homework


#admin.site.register(Lessons)


@admin.register(Lessons)
class LessonsAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass

#admin.site.register(Teachers_paln)

@admin.register(Teachers_paln)
class Teachers_palnAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass

@admin.register(Marks)
class MarksAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    pass

admin.site.register(homework)
admin.site.register(stud_marks)
admin.site.register(table)
admin.site.register(Library)



#admin.site.register(Marks)
