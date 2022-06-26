from django.contrib import admin

# Register your models here.
from .models import *


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'groupid')
    list_display_links = ('id', 'question')
    # search_fields = ('title', 'content')
    # list_filter = ('title', 'time_create', 'is_published', 'cat')
    # list_editable = ('is_published',)
    # prepopulated_fields = {"slug": ('title',)}


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'answer')
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ('name', )}

class QuestAnswsAdmin(admin.ModelAdmin):
    list_display = ('questionid', 'answerid')
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ('name', )}



class QuestionGroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ('name', )}


class TestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'userid', 'time_create')
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ('name', )}



class TestResultsAdmin(admin.ModelAdmin):
    list_display = ('id', 'testid', 'questionid', 'is_passed', 'result')
    # list_display_links = ('name',)
    # search_fields = ('name',)
    # prepopulated_fields = {"slug": ('name', )}


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(QuestAnsws, QuestAnswsAdmin)
admin.site.register(QuestionGroups, QuestionGroupsAdmin)
admin.site.register(Tests, TestsAdmin)
admin.site.register(TestResults, TestResultsAdmin)
