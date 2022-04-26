from django.db import models
from django.conf import settings
from django.utils import timezone

class Message(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    to_user = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(blank=True, null=True)

    def send(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.message

# Create your models here.
