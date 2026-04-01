from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='subjects_images', blank=True, null=True)
    


    class Meta:
        db_table =  'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        
    def __str__(self):
        return f'{self.name}' 

    def get_absolute_url(self):
        return f'("category", kwargs={'category_slug':self.slug})'
        
class Subjects(models.Model):
    name = models.CharField(max_length=150, unique=False, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='subjects_images', blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')
    
    
    class Meta:
        db_table =  'subjects'
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    
    def __str__(self):
        return f'{self.name}' 
    
    def get_absolute_url(self):
        return f'("subjects", kwargs={'subjects_slug':self.slug})'
    

class Teachers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='Teachers_images', blank=True, null=True)


    class Meta:
        db_table =  'teachers'
        verbose_name = 'учителя'
        verbose_name_plural = 'учителя'

    def __str__(self):
        return f'{self.name}' 
    
    def get_absolute_url(self):
        return f'("teacher", kwargs={'teacher_slug':self.slug})'

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
    
    def get_absolute_url(self):
        return f'("about_us", kwargs={'about_us_slug':self.slug})'