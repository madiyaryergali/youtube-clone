from django.db import models
from user.models import User

class Channel(models.model):
    channel_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField()
    background = models.ImageField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)