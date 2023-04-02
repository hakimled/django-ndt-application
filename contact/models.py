from django.db import models
from django.utils import timezone



class Message(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField(blank=False , null=False)
    message_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f'{self.first} {self.last} sent a message'