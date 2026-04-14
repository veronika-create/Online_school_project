from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True, db_index=True)
    groups= models.ManyToManyField(Permission, verbose_name='brabrabra', blank=True, help_text='Specific Permissions for this user.', related_name='brabrabra')
    user_permissions = models.ManyToManyField(Permission, verbose_name='abracadabra', blank=True, help_text='Specific Permissions for this user.', related_name='abracadabra')


    class Meta:
        db_table =  'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        swappable = 'AUTH_USER_MODEL'
        
    def _str__(self):
        return f'{self.username}' 

#class Registed_users(models.Model):
    #name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    #slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, #verbose_name='URL')



    #class Meta:
        #db_table =  'registed_users'
         #verbose_name = 'зарегистрированный пользователь'
         #verbose_name_plural = 'зарегистрированные пользователи'

     #def __str__(self):
         #return f'{self.name}' 
        
class List_of_teachers(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
   
    
    
    class Meta:
        db_table =  'List_of_teachers'
        verbose_name = 'список преподавателей'
        verbose_name_plural = 'списки преподавателей'

    
    def __str__(self):
        return f'{self.name}' 
    
class List_of_teachers_for_goups (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    category = models.ForeignKey(to= List_of_teachers , on_delete=models.CASCADE, verbose_name='список преподавателей')
    
    
    class Meta:
        db_table =  'List_of_teachers_for_groups'
        verbose_name = 'список преподавателей по группам'
        verbose_name_plural = 'списки преподавателей по группам'

    
    def __str__(self):
        return f'{self.name}' 
    
class List_of_students (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    
    
    class Meta:
        db_table =  'List_of_students'
        verbose_name = 'список студентов'
        verbose_name_plural = 'списки студентов'

    
    def __str__(self):
        return f'{self.name}' 