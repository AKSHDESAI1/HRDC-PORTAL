from operator import mod
from rest_framework import serializers
from App.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'