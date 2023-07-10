from django.db import models
from user.models import User

class Channel(models.Model):
    channel_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='images_uploaded', null=True)
    background = models.ImageField(upload_to='images_uploaded', null=True)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)