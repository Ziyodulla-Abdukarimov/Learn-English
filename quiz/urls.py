from django.urls import path
from .views import list_quizzes, correct, wrong

urlpatterns = [
    path('list-quizzes/', list_quizzes, name='list-quizzes'),
    path('correct/', correct, name="correct"),
    path('wrong/', wrong, name="wrong")
]
