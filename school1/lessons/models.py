from django.db import models



class Lessons(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
    
    
    class Meta:
        db_table =  'lessons'
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

    
    def __str__ (self):
        return f'{self.name}' 


class Marks(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
    
    
    class Meta:
        db_table =  'marks'
        verbose_name = 'оценка'
        verbose_name_plural = 'Оценки'

    
    def __str__ (self):
        return f'{self.name}'


class Teachers_paln(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
    
    
    class Meta:
        db_table =  'Plan'
        verbose_name = 'План'
        verbose_name_plural = 'Планы'

    
    def __str__ (self):
        return f'{self.name}'
    
class homework (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Тема')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Дз')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
     
    def __str__ (self):
        return f'{self.name}'
    
class  stud_marks(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Тема')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='уч.оценки')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
     
    def __str__ (self):
        return f'{self.name}'
    

class table(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Группа')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Расписание')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
     
    def __str__ (self):
        return f'{self.name}'
    
class  Library(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='предмет')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='библиотека')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)
     
    def __str__ (self):
        return f'{self.name}'