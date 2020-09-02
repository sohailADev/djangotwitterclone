from tweet import models


def tweet_count(request):
    total_tweets = models.Tweet.objects.count()

    return {"total_tweets":total_tweets}