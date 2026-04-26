from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    question = models.TextField(blank=True, null=True, verbose_name='Вопрос')
    option1 = models.TextField(blank=True, null=True, verbose_name='Первый вариант')
    option2 = models.TextField(blank=True, null=True, verbose_name='Второй вариант')
    option3 = models.TextField(blank=True, null=True, verbose_name='Третий вариант')
    option4 = models.TextField(blank=True, null=True, verbose_name='Четвёртый вариант')
    answer = models.TextField(blank=True, null=True, verbose_name='Верный ответ')

    class Meta:
        db_table =  'test'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        
    def __str__(self):
        return f'{self.name}' 
