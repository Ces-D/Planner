from django.urls import path, include

from .views import *

urlpatterns = [
    path("course/", CourseList.as_view()),
    path("course/<int:pk>", CourseDetail.as_view()), # expected to be called with keyword argument pk
    path("assignment/", CourseAssignmentList.as_view()),
    path("assignment/<int:pk>", CourseAssignmentDetail.as_view()), # expected to be called with keyword argument pk
    path("event/", EventList.as_view()),
    path("event/<int:pk>", EventDetail.as_view()), # expected to be called with keyword argument pk
]
