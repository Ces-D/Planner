from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status, generics

from .models import Course, CourseAssignment, Event
from .serializers import CourseAssignmentSerializer, CourseSerializer, EventSerializer


class CourseList(generics.ListCreateAPIView):
    """"
    Look at and create Course objects
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific Course objects
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAssignmentList(generics.ListCreateAPIView):
    """"
    Look at and create CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    serializer_class = CourseAssignmentSerializer


class CourseAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    serializer_class = CourseAssignmentSerializer


class EventList(generics.ListCreateAPIView):
    """"
    Look at and create Event objects
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update or Delete specific Event objects
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
