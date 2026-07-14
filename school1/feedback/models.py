from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='ФИО')
    email = models.CharField(max_length=150, unique=True, verbose_name='Email')
    description = models.CharField(max_length=150, unique=True, verbose_name='Текст собщения')
   
    

    class Meta:
        db_table =  'feedback'
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        
    def __str__(self):
        return f'{self.name}' 
    

class From_customers_qestions(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Тема')
    description = models.CharField(max_length=150, unique=True, verbose_name='Текст собщения')
   

    class Meta:
        db_table =  'questions_custoumers'
        verbose_name = 'Вопросуч'
        verbose_name_plural = 'Вопросыуч'
        
    def __str__(self):
        return f'{self.name}' 