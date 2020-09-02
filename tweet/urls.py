
from django.urls import path
from . import views
urlpatterns = [
    path('addtweet/', views.add_tweet_view,name="add_tweet_page"),
    path('tweet/<int:tweet_id>', views.tweet_detail_view,name="tweet_detail_page"),
 
]
