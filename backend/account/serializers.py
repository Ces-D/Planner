from .models import Account
from rest_framework.authtoken.serializers import serializers

from backend.planner.models import Course, Event

class AccountSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    event = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())

    class Meta:
        model = Account
        fields = ['email', 'username', 'course', 'event']