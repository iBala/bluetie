from rest_framework import serializers
from exam.models import question, exam, answer

class QuestionSerializer(serializers.ModelSerializer):
    # Serializer for Question models
    class Meta:
        model = question
        fields = ('question_text', 'user', 'answer_type', 'correct_answer')


class ExamSerializer(serializers.ModelSerializer):
    # Serializer for Exam models
    class Meta:
        model = exam
        fields = ('reattempt_allowed', 'user', 'questions')

class AnswerSerializer(serializers.ModelSerializer):
    # Serializer for Exam models
    class Meta:
        model = answer
        fields = ('answer_given', 'user', 'question')