from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status, generics

from .models import Course, CourseAssignment, Event
from .serializers import CourseAssignmentSerializer, CourseSerializer, EventSerializer


class CourseList(generics.ListCreateAPIView):
    """"
    Look at and create Course objects
    """
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.filter(account=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific Course objects
    """
    queryset = Course.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = CourseSerializer


class CourseAssignmentList(generics.ListCreateAPIView):
    """"
    Look at and create CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    serializer_class = CourseAssignmentSerializer

    def get_queryset(self):
        user_courses = Course.objects.filter(
            account=self.request.user)
        user_course_assignment = CourseAssignment.objects.get(course=user_courses)
        pass

class CourseAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    lookup_url_kwarg='pk'
    serializer_class = CourseAssignmentSerializer


class EventList(generics.ListCreateAPIView):
    """"
    Look at and create Event objects
    """
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(account=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update or Delete specific Event objects
    """
    queryset = Event.objects.all()
    lookup_url_kwarg='pk'
    serializer_class = EventSerializer
