from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')



    class Meta:
        db_table =  'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}' 
        
class Subjects(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='subjects_images', blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    
    class Meta:
        db_table =  'subjects'
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'

    
    def __str__(self):
        return f'{self.name}' 
    

class Teachers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='Teachers_images', blank=True, null=True)


    class Meta:
        db_table =  'teacher'
        verbose_name = 'учителю'
        verbose_name_plural = 'учителя'

    def __str__(self):
        return f'{self.name}' 
    

class About_us(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='About_us_images', blank=True, null=True)


    class Meta:
        db_table =  'about_us'
        verbose_name = 'о_нас'
        verbose_name_plural = 'о_нас'

    def __str__(self):
        return f'{self.name}' 