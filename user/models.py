from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    