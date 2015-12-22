from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Question(BaseModel):
    title = models.CharField(max_length=120, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

    def create_dict(self):
        return {
            'user': {
                'id': self.user.id,
                'name': self.user.username,
            },
            'id': self.id,
            'title': self.title,
        }


class Answer(BaseModel):
    title = models.CharField(max_length=120, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def create_dict(self):
        return {
            'question': {
              'id': self.question.id,
              'title': self.question.title,
            },
            'id': self.id,
            'title': self.title,
            'is_correct_answer': self.is_correct_answer,
        }


