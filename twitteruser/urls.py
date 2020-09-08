
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name="home_page"),
    path('profile/<str:user_name>/', views.ProfileView.as_view(),name="profile_page"),
    path('follow/<str:user_name>/', views.FollowView.as_view(),name="follow_page"),
    path('unfollow/<str:user_name>/', views.UnFollowView.as_view(),name="unfollow_page"),
]
