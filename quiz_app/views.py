from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Question


@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    # Create User Data
    user_dict = {
        'username': user.username,
    }

    # Create Question Array
    questions_for_user = Question.objects.filter(user=user)
    questions_array = []

    for question in questions_for_user:
        questions_array.append(question.create_dict())

    data = {
        'user': user_dict,
        'questions': questions_array,
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_questions(request):
    questions = Question.objects.all()

    questions_array = []

    for question in questions:
        questions_array.append(question.create_dict())

    data = {
        'questions': questions_array,
        'count': len(questions),
    }
    return Response(data, status=status.HTTP_200_OK)
