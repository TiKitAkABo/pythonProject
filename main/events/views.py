from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied, ValidationError

from .models import Attendees, Event
from .permissions import IsConfirmedOrReadOnly, IsOrganizerOrReadOnly
from .serializers import (EventSerializer, confirmAttendanceSerializer)


# Create your views here.
class EventListCreateAPIView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    def perform_create(self, serializer):
        organizer = self.request.user
        if organizer.profile.is_creator:
            serializer.save(organizer=organizer)
        else:
            raise PermissionDenied("You are not authorized to create Events. Update your profile!")

    def perform_destroy(self, instance):
        Event_instance = self.get_object()
        user = self.request.user
        organizer = Event_instance.organizer

        if user !=organizer:
            raise ValidationError("Sorry you are not authorized to delete this Event!")
        Event_instance.delete()


class confirmAttendanceAPIView(viewsets.ModelViewSet):
    queryset = Attendees.objects.all()
    serializer_class = confirmAttendanceSerializer
    permission_classes = [IsConfirmedOrReadOnly]

    def perform_create(self, serializer):
        print(self.request.data['event'])
        attendance_queryset = Attendees.objects.filter(event=self.request.data['event'],
        user=self.request.user)

        if attendance_queryset.exists() :
            raise ValidationError('you already booked this event.')
        serializer.save(user=self.request.user)
