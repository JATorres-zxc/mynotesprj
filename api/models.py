from django.db import models

# Create your models here.

# DATABASE REPLICA
class Note(models.Model):
    body = models.TextField(null=True, blank=True) # store content
    updated = models.DateTimeField(auto_now = True) # when it is updated
    created = models.DateTimeField(auto_now_add =True) # when it is created
    
    def __str__(self) -> str:
        return self.body[:50] if self.body else "Untitled Note" # return first 50 else untitled note
    