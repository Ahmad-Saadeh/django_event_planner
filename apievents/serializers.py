from rest_framework import serializers
from events.models import Event,Booking

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields=["id","title","description","location","datetime","seats","added_by"]
