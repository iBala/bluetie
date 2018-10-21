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
class QuestionList(viewsets.ViewSet):
    @list_route(
        methods=['get', 'post'],
        url_path='question',
        url_name='question',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        query_set = question.objects.all()
        serializer = QuestionSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Exam/
class ExamList(APIView):
    @list_route(
        methods=['get', 'post'],
        url_path='exam',
        url_name='exam',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        query_set = exam.objects.all()
        serializer = ExamSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Answer/
class AnswerList(APIView):
    @list_route(
        methods=['get', 'post'],
        url_path='answer',
        url_name='answer',
        permission_classes=(IsLoggedInUser,),
    )
    def get(self, request):
        query_set = answer.objects.all()
        serializer = AnswerSerializer(query_set, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)