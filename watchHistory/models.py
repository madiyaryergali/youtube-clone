from django.db import models
from user.models import User
from video.models import Video

class WatchHistory(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    watch_date = models.DateTimeField(auto_now_add=True)
    video_id = models.ForeignKey(Video, on_delete=models.PROTECT)

