from django.shortcuts import render, redirect, get_object_or_404

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from .models import Course, CourseAssignment, Event
from .serializers import CourseAssignmentSerializer, CourseSerializer, EventSerializer


class CourseList(generics.ListCreateAPIView):
    """"
    Look at and create Course objects
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific Course objects
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseAssignmentList(generics.ListCreateAPIView):
    """"
    Look at and create CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    serializer_class = CourseAssignmentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # print("\n\n\n", serializer.data, "\n\n\n", headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        

class CourseAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update, or Delete specific CourseEvent objects
    """
    queryset = CourseAssignment.objects.all()
    serializer_class = CourseAssignmentSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EventList(generics.ListCreateAPIView):
    """"
    Look at and create Event objects
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """"
    Get, Update or Delete specific Event objects
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

