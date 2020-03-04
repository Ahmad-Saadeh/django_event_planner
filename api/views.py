from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView,RetrieveAPIView
from events.models import Event, Booking
from .serializer import ListSerializer, ListEventsSerializer, RegisterSerializer, EventSerializer, BookSerializer, BookEventSerializer, EventUsersSerializer
from datetime import datetime
from .permissions import IsEventOwner

class UpdateView(RetrieveUpdateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'
	permission_classes=[IsAuthenticated]

class EventCreateView(CreateAPIView):
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class ListView(ListAPIView):
	serializer_class=ListSerializer
	permission_classes=[AllowAny]
	def get_queryset(self):
		return Event.objects.filter(datetime__gte=datetime.today())

class ListEventsView(ListAPIView):
	serializer_class=ListEventsSerializer
	permission_classes= [IsAuthenticated]
	def get_queryset(self):
		return Event.objects.filter(added_by=self.request.user, datetime__gte=datetime.today())

class Register(CreateAPIView):
	queryset=User.objects.all()
	serializer_class = RegisterSerializer
	# permission_classes=[AllowAny]

class BookEventList(ListAPIView):
	permission_classes=[IsAuthenticated]
	serializer_class=BookSerializer
	def get_queryset(self):
		return Booking.objects.filter(booker=self.request.user)

class Book(CreateAPIView):
	serializer_class=BookEventSerializer
	permission_classes=[IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(booker=self.request.user)

class EventUsers(ListAPIView):
	# queryset=Booking.objects.all()
	def get_queryset(self):
		event=Event.objects.get(id=self.kwargs.get('event_id'))
		return Booking.objects.filter(event=event)
	serializer_class=EventUsersSerializer
	permission_classes=[IsEventOwner]
