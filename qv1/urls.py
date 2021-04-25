from django.urls import path
from qv1.views import *
urlpatterns = [
    path('quizzes/', QuizView.as_view(), name="quizzes")
]