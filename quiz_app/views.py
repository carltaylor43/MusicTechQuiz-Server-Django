from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Question
from .serializer import UserSerializer


@api_view(['GET'])
def get_user(request, username):
    user = User.objects.filter(username=username)
    user_serializer = UserSerializer(user, many=True)

    questions_for_user = Question.objects.filter(user=user)

    array = []

    for question in questions_for_user:
        array.append(question.create_dict())

    data = {
        'user': user_serializer.data,
        'questions': array,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_questions(request):
    questions = Question.objects.all()
    # serializer = QuestionSerializer(questions, many=True)
    boom = {'name': 'bob'}

    data = {
        'questions': boom,
        'count': len(questions),
    }
    return Response(data, status=status.HTTP_200_OK)
