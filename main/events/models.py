from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=250)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizer")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    day_of_event = models.DateTimeField(auto_now=True)
    attendees = models.ManyToManyField(User, related_name="attendees", through='Attendees')

    def __str__(self):
        return self.name


class Attendees(models.Model): # модель уведомления о присутствии.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_many')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_many')

    class Meta:
        verbose_name_plural = "Attendees"

    def __str__(self):
        return self.user.username + " - " + self.event.name