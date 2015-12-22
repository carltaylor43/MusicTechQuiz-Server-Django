from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.StackedInline):
    model = Answer
    fk_name = 'question'
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        ]

admin.site.register(Question, QuestionAdmin)

