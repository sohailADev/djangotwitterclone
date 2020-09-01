from django.db import models
from twitteruser.models import  TwitterUserModel
# Create your models here.
class Tweet(models.Model):
    tweet_content = models.CharField(max_length=140)
    created_at    = models.DateField(auto_now_add=True)
    tweet_user    = models.ForeignKey(TwitterUserModel , on_delete=models.CASCADE)