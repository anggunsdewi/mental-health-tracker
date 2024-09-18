import uuid 
from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    time = models.DateField(auto_now_add=True)
    feelings = models.TextField()
    mood_intensity = models.IntegerField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    #test

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5