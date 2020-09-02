
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_view,name="home_page"),
    path('profile/<str:user_name>/', views.profile_view,name="profile_page"),
    path('follow/<str:user_name>/', views.follow_view,name="follow_page"),
    path('unfollow/<str:user_name>/', views.unfollow_view,name="unfollow_page"),
]
