from rest_framework import serializers
from .models import Question, Exam, Answer

class QuestionSerializer(serializers.ModelSerializer):
    # Serializer for Question models
    class Meta:
        model = Question
        fields = ('question_text', 'user', 'answer_type', 'correct_answer')


class ExamSerializer(serializers.ModelSerializer):
    # Serializer for Exam models
    class Meta:
        model = Exam
        fields = ('reattempt_allowed', 'agent', 'questions')

class AnswerSerializer(serializers.ModelSerializer):
    # Serializer for Exam models
    class Meta:
        model = Exam
        fields = ('answer_given', 'candidate', 'question')