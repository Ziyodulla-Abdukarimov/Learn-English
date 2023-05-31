from django.urls import path
from .views import home, courses, course_detail, about, manual

urlpatterns = [
    path('', home, name='main'),
    path('courses/', courses, name='courses'),
    path('courses/<int:pk>', course_detail, name='course-detail'),
    path('manual/',manual, name='manual'),
    path('about/', about, name='about'),

]
