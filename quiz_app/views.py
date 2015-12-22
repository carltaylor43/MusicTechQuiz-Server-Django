import datetime
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Question, Answer


@api_view(['GET'])
def get_user(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    # Create User Data
    user_dict = {
        'id': user.id,
        'name': user.username,
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

    for question_obj in questions:
        questions_array.append(question_obj.create_dict())

    data = {
        'questions': questions_array,
        'count': len(questions),
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    data = question.create_dict()
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_answer(request, answer_id):
    try:
        answer = Answer.objects.get(id=answer_id)
    except Answer.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    data = answer.create_dict()
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_updates_since(request, epoch_time):
    last_year = 1419243503
    client_last_updated = datetime.datetime.fromtimestamp(float(last_year))
    questions_ready_for_update = Question.get_updated_ids_since_time(client_last_updated)
    answers_ready_for_update = Answer.get_updated_ids_since_time(client_last_updated)
    data = {
        'question': questions_ready_for_update,
        'answer': answers_ready_for_update
    }
    return Response(data, status=status.HTTP_200_OK)
