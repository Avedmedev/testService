from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse


class Questions(models.Model):
    question = models.TextField(blank=True, verbose_name='Вопрос')
    groupid = models.ForeignKey('QuestionGroups', on_delete=models.CASCADE, null=True, verbose_name='Группы вопросов')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answers(models.Model):
    answer = models.CharField(max_length=255, verbose_name='Ответ')
    questionid = models.ForeignKey(Questions, on_delete=models.CASCADE,  verbose_name='Вариант ответа к вопросу')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

class QuestAnsws(models.Model):
    questionid = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Номер вопроса')
    answerid = models.ForeignKey(Answers, on_delete=models.CASCADE, verbose_name='Номер ответа')

    class Meta:
        verbose_name = 'вопрос-ответ'

class QuestionGroups(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя группы')
#    questionid = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Вариант ответа к вопросу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Tests(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время начала тестирования')
    
    def __str__(self):
        return self.userid

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class TestResults(models.Model):
    testid = models.ForeignKey(Tests, on_delete=models.CASCADE, verbose_name='Номер теста')
    questionid = models.ForeignKey(Questions, on_delete=models.CASCADE, verbose_name='Номер вопроса')
    is_passed = models.BooleanField(default=False, verbose_name='Вопрос пройден в данном тестировании')
    result = models.BooleanField(default=False, verbose_name='Правильно отвечен')
    

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

