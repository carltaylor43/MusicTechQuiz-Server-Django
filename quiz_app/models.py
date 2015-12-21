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

    def create_dict(self):
        json = {
            'id': self.id,
            'title': self.title,
        }
        return json


class Answer(BaseModel):
    title = models.CharField(max_length=120, default='')
    order_number = models.IntegerField()

    class Meta:
        ordering = ('order_number',)

