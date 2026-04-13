from django.db import models
from django.contrib.auth.models import User

class Events(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nameEvent = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    starts_at = models.DateTimeField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.nameEvent





class Ticket(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='tickets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.nameEvent}"