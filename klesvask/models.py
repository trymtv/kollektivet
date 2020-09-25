from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Wash(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    washType = models.CharField(max_length=100)
    degrees = models.IntegerField()
    washLength = models.IntegerField()
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(null=True)
    ongoing = models.BooleanField()

    def __str__(self):
        return self.user.first_name + " " + self.washType

class WashQueue(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    regDate = models.DateTimeField(default=timezone.now)
    washType = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username + ": " + self.washType
    