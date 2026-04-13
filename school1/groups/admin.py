from django.contrib import admin


from groups.models import Courses
from groups.models import Groups
from groups.models import Material_for_students
from groups.models import Base_of_knowledge
from groups.models import Lectures
from groups.models import Tests
from groups.models import Resulst
from groups.models import Questions
from groups.models import Choice 
from groups.models import Answer






@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'question',
        'choice',
    )
    list_filter = ('user',)




@admin.register(Resulst)
class ResulstAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'title',
        'visible',
        'max_points',
    )

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        'title',
        'question',
        'points',
        'lock_other',
    )
    list_filter = ('question',)

@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

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



