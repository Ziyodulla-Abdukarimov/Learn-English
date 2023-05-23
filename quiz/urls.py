from django.urls import path
from .views import list_quizzes

urlpatterns = [
    path('list-quizzes/', list_quizzes, name='list-quizzes')
]
