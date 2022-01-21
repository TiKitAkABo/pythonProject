from rest_framework import serializers
from .models import Event, Attendees


class EventSerializer(serializers.ModelSerializer):
    event = serializers.StringRelatedField(read_only=True, many=True)
    organizer = serializers.StringRelatedField(read_only=True)
    attendees = serializers.StringRelatedField(read_only=True, many=True)
    attendee_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'

    def get_attendee_count(self, object):
        return object.attendees.count()


class confirmAttendanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Attendees
        fields = '__all__'

