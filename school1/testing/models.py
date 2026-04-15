from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20)
    option2 = models.CharField(max_length = 20)
    option3 = models.CharField(max_length = 20)
    option4 = models.CharField(max_length = 20)
    answer = models.CharField(max_length = 20)

    class Meta:
        db_table =  'test'
        verbose_name = 'Теста'
        verbose_name_plural = 'Тысты'
        
    def __str__(self):
        return f'{self.name}' 