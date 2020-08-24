from django.urls import path, include

from .views import *

urlpatterns = [
    path("course/", CourseList.as_view()),
    path("course-detail/", CourseDetail.as_view()),
    path("assignment/", CourseAssignmentList.as_view()),
    path("assignment-detail/", CourseAssignmentDetail.as_view()),
    path("event/", EventList.as_view()),
    path("event-detail/", EventDetail.as_view()),
]
