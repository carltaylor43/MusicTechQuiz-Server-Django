from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Question


class UserSerializer(serializers.ModelSerializer):

    # questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')