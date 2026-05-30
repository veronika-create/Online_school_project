from django.db import models



class Test(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    question = models.TextField(blank=True, null=True, verbose_name='Вопрос')
    option1 = models.CharField(blank=True, null=True, verbose_name='Первый вариант')
    option2 = models.CharField(blank=True, null=True, verbose_name='Второй вариант')
    option3 = models.CharField(blank=True, null=True, verbose_name='Третий вариант')
    option4 = models.CharField(blank=True, null=True, verbose_name='Четвёртый вариант')
    option1_count = models.IntegerField(blank=True, null=True, verbose_name='Первый ответ')
    option2_count = models.IntegerField(blank=True, null=True, verbose_name='Второй ответ')
    option3_count = models.IntegerField(blank=True, null=True, verbose_name='Третий ответ')
    option4_count = models.IntegerField(blank=True, null=True, verbose_name='Четвёртый ответ')

    class Meta:
        db_table =  'test'
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        
    def __str__(self):
        return f'{self.name}' 

    def total (self):
        return self.option1_count+self.option2_count+self.option3_count+ self.option4_count