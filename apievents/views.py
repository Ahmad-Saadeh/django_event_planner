from django.shortcuts import render
from rest_framework.generics import ListAPIView
from events.models import Event,Booking
from .serializers import EventSerializer

class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
