from django.contrib import admin


from testing.models import Test, Question, Answer, Choice, Result, TestQuestion, UserAnswer, TestChoice


admin.site.register (Test)

class TestAdmin(admin.ModelAdmin):
	list_display = ('question',)

admin.site.register(Question)
admin.site.register(Result)

admin.site.register(Answer)
admin.site.register(Choice)

admin.site.register(TestQuestion)
admin.site.register(UserAnswer)
admin.site.register(TestChoice)