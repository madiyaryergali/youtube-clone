from django.db import models
from user.models import User
from video.models import Video

class SavedVideos(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.PROTECT)
