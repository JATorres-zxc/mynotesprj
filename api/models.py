from django.db import models

# Create your models here. DATABASE REPLICA

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add =True)
    
    def __str__(self) -> str:
        return self.body[:50] if self.body else "Untitled Note"
    