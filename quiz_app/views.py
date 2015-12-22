import datetime
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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


@api_view(['POST'])
def post_question(request):

    request_data = request.data
    user_name = request_data['user_name']
    question_title = request_data['question']
    answers_dict = request_data['answers']

    user = User.objects.get(username=user_name)
    question = Question(user=user, title=question_title)
    try:
        question.save()
    except Exception:
        # todo: get validation exception
        data = {'message': 'Question already exists'}
        return Response(data, status=status.HTTP_200_OK)

    for answer_title in answers_dict:
        correct_answer = answers_dict[answer_title]
        if correct_answer == 'True':
            is_correct = True
        else:
            is_correct= False
        new_answer = Answer(question=question, title=answer_title, is_correct_answer=is_correct)
        new_answer.save()

    data = {'message': 'Successfully added Question to online database'}
    return Response(data, status=status.HTTP_200_OK)

# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))

@api_view(['DELETE'])
def delete_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    question.delete()
    data = {'message': 'Successfully deleted Question from online database'}
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def login_user(request):
    user_data = request.data
    user_name = user_data['user_name']
    try:
        user = User.objects.get(username=user_name)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)
    # todo: check password
    token = user.auth_token
    token.delete()
    token = Token.objects.create(user=user)
    data = {
        'message': 'Successfully logged in',
        'token': token.key
    }
    return Response(data, status=status.HTTP_200_OK)



# todo: consider adding PUT methods for updating questions and answers for user
