from rest_framework.serializers import ModelSerializer
from .models import Quiz, Question


class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        # fields = ('name', 'description')
        exclude=('url',)

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
