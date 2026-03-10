from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='lessons_images', blank=True, null=True)

    class Meta:
        db_table =  'category'
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'
    
    def __str__(self):
        return self.name
