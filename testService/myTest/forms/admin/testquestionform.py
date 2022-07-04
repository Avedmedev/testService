from django import forms
from django.contrib import admin
from django.contrib.admin import widgets
from myTest.models import Test, Question, Answer, TestQuestion



class TestQuestionAnswerForm(forms.ModelForm):

    answerid = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('answerid', False), 
        queryset=Answer.objects.all()
        )
    
    answerid1 = forms.ModelMultipleChoiceField(
        widget=widgets.FilteredSelectMultiple('name', False), 
        queryset=Answer.objects.all()
        )

    class Meta:
        model = TestQuestion
        exclude = ('',)

class TestQuestionAnswerFormAdmin(admin.ModelAdmin):

    class Meta:
        form = TestQuestionAnswerForm

