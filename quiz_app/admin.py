from django.contrib import admin
from .models import Question, Answer, Score


class AnswerInline(admin.StackedInline):
    model = Answer
    fk_name = 'question'
    max_num = 4
    min_num = 4


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
        ]


class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Score, ScoreAdmin)

