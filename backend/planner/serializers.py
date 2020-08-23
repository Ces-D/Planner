from rest_framework import serializers

from .models import Course, CourseAssignment, Event

class CourseSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default= serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ('__all__')


class CourseAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAssignment
        fields=('__all__')


class EventSerializer(serializers.ModelSerializer):
    account = serializers.HiddenField(default= serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = ("__all__")