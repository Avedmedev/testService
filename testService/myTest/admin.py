from cProfile import label
from dataclasses import field
from msilib.schema import SelfReg
from traceback import print_tb
from django.contrib import admin
from django import forms

from django.contrib.admin import widgets

from django.contrib.auth.models import Group

from .models import *



admin.site.register(UserTest)
admin.site.register(TestResults)
admin.site.unregister(Group)


class MyTeAdminForm(forms.ModelForm):
    
    right_answer = forms.ModelMultipleChoiceField(
        label='Правильные ответы',
        widget=widgets.FilteredSelectMultiple(verbose_name='Правильные ответы', is_stacked=False),
        queryset=Ans.objects.all(), 
        blank=True
    )
    
    def __init__(self, *args, **kwargs) -> None:
        super(MyTeAdminForm, self).__init__( *args, **kwargs)

        if self.instance and self.instance.pk:
            
            self.fields['right_answer'] = forms.ModelMultipleChoiceField(
                queryset=Ans.objects.filter(teques=self.instance.pk),           #набор ответов для вопроса для данного теста. В другом тесте набор ответов может отличаться
                required=False
                )
            all = list(Ans.objects.filter(teques=self.instance.pk).values_list('id',flat=True))
            selected = list(Ans.objects.filter(ques=self.instance.questionid_id).values_list('id',flat=True))
            self.fields['right_answer'].initial = [a for a in selected if a in all]
            

    def save(self, commit: bool = ...):

        if self.instance:
            
            quest = Ques.objects.filter(text=self.cleaned_data['questionid']).first()
            
            #delete all previous right_answer
            quest.r_answer.clear()

            for a in self.cleaned_data['right_answer']:
                quest.r_answer.add(a)

        return super().save(commit)


    def clean_right_answer(self):
        
        if len(self.fields['right_answer'].queryset) == 0:
            return self.cleaned_data['right_answer']
        if len(self.cleaned_data['right_answer']) == 0:
            raise forms.ValidationError('Выберите один или несколько ответов')        
        if len(self.cleaned_data['right_answer']) == len(self.fields['right_answer'].queryset) and len(self.fields['right_answer'].queryset) > 1:
            raise forms.ValidationError('Все значения не могут быть правильными ответами')        
    
        return self.cleaned_data['right_answer']


class TeQuesInline(admin.TabularInline):
    model = TeQues
    form = MyTeAdminForm
    
    formfield_overrides = {
        models.TextField: {'widget': widgets.FilteredSelectMultiple},
    }
    filter_horizontal = ['answer']
    fields = ['questionid', 'answer', 'right_answer'] 
    extra = 0
    show_change_link = True


class TeAdmin(admin.ModelAdmin):
    model = Te
    inlines = [TeQuesInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

class QuesAdmin(admin.ModelAdmin):
    model = Ques
    fields = ['text']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


admin.site.register(Ans)
admin.site.register(Ques, QuesAdmin)
admin.site.register(Te, TeAdmin)
