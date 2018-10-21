from django.shortcuts import render
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from exam.models import question, answer, exam
from exam.serializers import QuestionSerializer, ExamSerializer, AnswerSerializer
from users.permissions import IsLoggedInUser
from rest_framework import generics, viewsets, exceptions, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
# Question/
class GetQuestionAPI(viewsets.ViewSet):
    @list_route(
        methods=['get', 'post'],
        url_path='question',
        url_name='question',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        # query_set = question.objects.all()
        query_set = question.objects.filter(user = request.user)
        serializer = QuestionSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetQuestionWithId(viewsets.ViewSet):
    @list_route(
        methods=['get'],
        url_path='question',
        url_name='question',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        # query_set = question.objects.all()
        query_set = question.objects.filter(user=request.user, id=request.data.id)
        serializer = QuestionSerializer(query_set, many=True)
        return Response(serializer.data)

# Exam/
class GetExamAPI(viewsets.ViewSet):
    @list_route(
        methods=['get', 'post'],
        url_path='exam',
        url_name='exam',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        # query_set = exam.objects.all()
        query_set = exam.objects.filter(user=request.user)
        serializer = ExamSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetExamWithId(viewsets.ViewSet):
    @list_route(
        methods=['get'],
        url_path='exam',
        url_name='exam',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        # query_set = exam.objects.all()
        query_set = exam.objects.filter(user=request.user, id=request.data.id)
        serializer = ExamSerializer(query_set, many=True)
        return Response(serializer.data)

# Answer/
class GetAnswerAPI(viewsets.ViewSet):
    @list_route(
        methods=['get', 'post'],
        url_path='answer',
        url_name='answer',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        query_set = answer.objects.filter(question=request.data.question)
        serializer = AnswerSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)