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

    def queryset(self, request):
        qs = super(QuestionAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ScoreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Question, QuestionAdmin)
admin.site.register(Score, ScoreAdmin)

