from django.db import models
from django.conf import settings 
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

class Question(models.Model):
    class qtype(models.TextChoices):
        single = 'single'
        multiple = 'multiple'
   
    name = models.CharField(max_length=350,  blank=True, unique=True, verbose_name='Название')
    qtype = models.CharField(max_length=8, choices=qtype.choices, default=qtype.single)
    explanation = models.CharField(max_length=550, blank=True, unique=True)


    def get_answers(self):
        if self.qtype == 'single':
            return self.answer_set.filter(is_correct=True).first()
        else:
            qs = self.answer_set.filter(is_correct=True).values()
            return [i.get('name') for i in qs]


    def user_can_answer(self, user):
        user_choices = user.choice_set.all()
        done = user_choices.filter(question=self)
        print(done)
        if done.exists():
            return False
        return True

    def __str__(self):
        return f'{self.name}' 

    class Meta:
        ordering = ['id']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, unique=True )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}' 

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class Choice(models.Model):
    #user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,  on_delete=models.CASCADE)
     
class Result(models.Model):
    #user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)





class TestQuestion(models.Model):
    text = models.CharField(max_length=500)
    is_multiple_choice = models.BooleanField(default=False)  # если нужно

    def __str__(self):
        return self.text

class TestChoice(models.Model):
    question = models.ForeignKey(TestQuestion, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} – {self.text}"

class UserAnswer(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(TestChoice, on_delete=models.SET_NULL, null=True)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')  # один ответ на вопрос от пользователя

