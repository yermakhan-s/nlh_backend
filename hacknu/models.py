from django.db import models
from authentication.models import User

# Create your models here.

class QuizStatement(models.Model):
    class TYPES:
        READING = 0
        GRAMMAR = 1
        DICTANT = 2
        TYPE_CHOICES = [(READING, 'Оқылым'), (GRAMMAR, 'Грамматика'), (DICTANT, 'Диктант')]


    title = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    quiz_type = models.IntegerField(choices=TYPES.TYPE_CHOICES, default=0, verbose_name='Тип')

class QuizQuestions(models.Model):
    quiz_statement = models.ForeignKey(QuizStatement, on_delete=models.CASCADE, null=True, blank=True,  related_name='questions')
    question = models.CharField(max_length=200, null=True, blank=True)
    a = models.CharField(max_length=200, null=True, blank=True)
    b = models.CharField(max_length=200, null=True, blank=True)
    c = models.CharField(max_length=200, null=True, blank=True)
    d = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)

class QuizInstance(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  related_name='quizzes')
    quiz_statement = models.ForeignKey(QuizStatement, on_delete=models.CASCADE, null=True, blank=True, related_name='results')
    percentage = models.IntegerField(blank=True, null=True)
    taken_date = models.DateTimeField('Дата и время прохождения', null=True, auto_now_add=True)