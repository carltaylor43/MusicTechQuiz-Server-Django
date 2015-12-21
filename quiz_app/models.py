from django.db import models


class Question(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=120)

    class Meta:
        ordering = ('created',)

