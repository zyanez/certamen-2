from django.db import models
import uuid

class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content