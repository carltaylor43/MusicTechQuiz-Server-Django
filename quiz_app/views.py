from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Question
from .serializer import QuestionSerializer, UserSerializer


@api_view(['GET'])
def get_user(request, username):
    user = User.objects.filter(username=username)
    serializer = UserSerializer(user, many=True)
    data = {
        'user': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    data = {
        'questions': serializer.data,
        'count': len(questions),
    }
    return Response(data, status=status.HTTP_200_OK)
