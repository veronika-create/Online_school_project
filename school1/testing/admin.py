from django.contrib import admin


from testing.models import Test, Question, Answer, Choice, Result, TestQuestion, UserAnswer, TestChoice





admin.site.register(TestQuestion)
admin.site.register(UserAnswer)
admin.site.register(TestChoice)