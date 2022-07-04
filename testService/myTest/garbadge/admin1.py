from django.contrib import admin

from django import forms

from betterforms.multiform import MultiModelForm

# Register your models here.
from ..models import *

import django.apps

models = django.apps.apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


class QuestsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(QuestsForm, self).__init__( *args, **kwargs)
        #self.fields['answers'].help_text = 'Удерживайте ctrl, чтобы выбрать несколько вариантов ответа на вопрос выше'
        #print(self.fields['answers'].widget_attrs)
        
    class Meta:
        model = Quests
        exclude = ('',)

class AnswersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(AnswersForm, self).__init__( *args, **kwargs)
        self.fields['answers'].help_text = 'Удерживайте ctrl, чтобы выбрать несколько вариантов ответа на вопрос выше'
        #print(self.fields['answers'].widget_attrs)
        
    class Meta:
        model = Answers
        exclude = ('',)


class QuestionAnswerMultiForm(MultiModelForm, forms.ModelForm):
    form_classes = {
        'question': QuestsForm,
        'answer': AnswersForm,
    }

class QuestsFormAdmin(admin.ModelAdmin):
    form = QuestionAnswerMultiForm
    #form = AnswersForm
        

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')
    list_display_links = ('id', 'question')
    # search_fields = ('title', 'content')
    # list_filter = ('title', 'time_create', 'is_published', 'cat')
    # list_editable = ('is_published',)
    # prepopulated_fields = {"slug": ('title',)}
    # change_list_template = "path to to .html in templates/amin/..."


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer')
    # list_display_links = ('name',)

class QuestAnswsAdmin(admin.ModelAdmin):
    list_display = ('questionid', 'answerid')

class QuestionGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)

class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'time_create')

class TestResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'testid', 'questionid', 'is_passed', 'result')

#admin.site.register(Questions, QuestionsAdmin)
#admin.site.register(Answers)
admin.site.register(QuestAnsws, QuestAnswsAdmin)
admin.site.register(QuestionGroups, QuestionGroupsAdmin)
admin.site.register(Tests, TestsAdmin)
admin.site.register(TestResults, TestResultsAdmin)
admin.site.register([Quests, Answers], QuestsFormAdmin)
