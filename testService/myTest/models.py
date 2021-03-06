from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User

from django.contrib.contenttypes.fields import GenericForeignKey, ContentType

from django.urls import reverse


class UserTest(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    testid = models.ForeignKey('Te', on_delete=models.CASCADE, verbose_name='Тест')
    score = models.FloatField(verbose_name='Результат, %')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время начала тестирования')
        
    def __str__(self):
        return self.userid

    class Meta:
        verbose_name = 'Результат пользователя'
        verbose_name_plural = 'Результаты пользователей'

class TestResults(models.Model):
    testquestionid = models.ForeignKey('TeQues', on_delete=models.CASCADE, verbose_name='Вопрос теста')
#    questionid = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Номер вопроса')
#    is_passed = models.BooleanField(default=False, verbose_name='Вопрос пройден в данном тестировании')
    result = models.BooleanField(default=False, verbose_name='Правильно отвечен')
    

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

"""
    Student (id, ...)
    StudentTest (id, studentId, testId, date, score, passYN,....)
    StudentTestQuestion (id, studentTestId, testQuestionId)
    StudentTestQuestionAnswer (id, studentTestQuestionId, answerId)
"""

class Ans(models.Model):
    text = models.CharField(max_length=255, verbose_name='Варианты ответа')
    #questionid = models.ForeignKey('Ques', on_delete=models.CASCADE, verbose_name='Ans')

    def __str__(self):
        return self.text


class TeQues(models.Model):
    testid = models.ForeignKey('Te', on_delete=models.CASCADE, verbose_name='Тест')
    questionid = models.ForeignKey('Ques', on_delete=models.CASCADE, verbose_name='Вопрос теста')
    answer = models.ManyToManyField('Ans', verbose_name='Варианты ответа')

    def __str__(self):
        return str(self.testid)


class Ques(models.Model):
    text = models.CharField(max_length=255, verbose_name='Te')
    r_answer = models.ManyToManyField('Ans')

    def __str__(self):
        return self.text


class Te(models.Model):
    text = models.CharField(max_length=255, unique=True, verbose_name='Te')


    def __str__(self):
        return self.text
