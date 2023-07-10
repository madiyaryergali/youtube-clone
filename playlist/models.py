from django.db import models
from video.models import Video
from user.models import User

class Playlist(models.Model):
    playlist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
