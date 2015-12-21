from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Question(BaseModel):
    title = models.CharField(max_length=120, default='')

    class Meta:
        ordering = ('created',)


class Answer(BaseModel):
    title = models.CharField(max_length=120, default='')
    order_number = models.IntegerField()

    class Meta:
        ordering = ('order_number',)

