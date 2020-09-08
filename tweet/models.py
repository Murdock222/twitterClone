from django.db import models
from twitteruser.models import TwitterProfile
from django.utils import timezone

class Tweet(models.Model):
    author = models.ForeignKey(TwitterProfile, on_delete=models.CASCADE,)
    text = models.CharField(max_length=180)
    tweet_time = models.DateTimeField(defult=timezone.now)
