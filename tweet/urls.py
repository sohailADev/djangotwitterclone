
from django.urls import path
from . import views
urlpatterns = [
    path('addtweet/', views.AddTweetView.as_view(),name="add_tweet_page"),
    path('tweet/<int:tweet_id>', views.TweetDetailView.as_view(),name="tweet_detail_page"),
 
]
