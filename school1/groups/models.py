from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')



    class Meta:
        db_table =  'cours'
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

    def __str__(self):
        return f'{self.name}' 
        
class Groups(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='groups_images', blank=True, null=True)
    category = models.ForeignKey(to=Courses, on_delete=models.CASCADE, verbose_name='курс')
    
    
    class Meta:
        db_table =  'groups'
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    
    def __str__(self):
        return f'{self.name}' 
    
class Material_for_students(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(to=Courses, on_delete=models.CASCADE, verbose_name='курсы')
    
    
    class Meta:
        db_table =  'material_ofr_students'
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

    
    def __str__(self):
        return f'{self.name}' 
    


class Base_of_knowledge(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    

    class Meta:
        db_table =  'base_of_knowledge'
        verbose_name = 'база_знаний'
        verbose_name_plural = 'бау_знаний'

    def __str__(self):
        return f'{self.name}' 
    

class Lectures(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(to=Base_of_knowledge, on_delete=models.CASCADE, verbose_name='База знаний')


    class Meta:
        db_table =  'Lectures'
        verbose_name = 'Лекцию'
        verbose_name_plural = 'Лекции'

    def __str__(self):
        return f'{self.name}' 


class Tests(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Вопрос')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table =  'tests'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self):
        return f'{self.name}' 
    


class Questions (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название вопроса')
    question_text = models.CharField(max_length=500, verbose_name='Текст вопроса')
    more_text = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Доп. инфо')
    category = models.ForeignKey(to=Tests, on_delete=models.CASCADE, verbose_name='База знаний')

    class Meta:
        db_table =  'question'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self):
        return f'{self.name}' 

class Choice (models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    question = models.ForeignKey(Questions,on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField(max_length=200,)
    bal = models.IntegerField()
    
    class Meta: 
        db_table =  'choice'
        verbose_name = 'варианты'
        verbose_name_plural = 'варианты'

    def __str__(self):
        return f'{self.name}' 
    
class Answer(models.Model):
    
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Questions, on_delete=models.DO_NOTHING)
    choice = models.ForeignKey(Choice, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice}' 

class Resulst(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey(to=Tests, on_delete=models.CASCADE, verbose_name='Тест')


    class Meta:
        db_table =  'results'
        verbose_name = 'результат'
        verbose_name_plural = 'результаты'

    def __str__(self):
        return f'{self.name}' 