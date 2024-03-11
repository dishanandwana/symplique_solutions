from django.db import models
from django.contrib.auth.models import User


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=False)
    time = models.TimeField(blank=False)
    message = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"Reminder for {self.user.username} on {self.date} at {self.time}: {self.message}"
