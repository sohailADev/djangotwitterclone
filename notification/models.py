from django.db import models
from tweet.models import Tweet
from twitteruser.models import TwitterUserModel


class Notification(models.Model):
    user_to_notify = models.ForeignKey(TwitterUserModel, on_delete=models.CASCADE, related_name="user_to_notify")
    tweet_to_be_notify = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="tweet_to_be_notify")
    notification_flag = models.BooleanField(default=False)