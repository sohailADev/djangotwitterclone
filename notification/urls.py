
from django.urls import path
from . import views
urlpatterns = [
    path('notifications/', views.notification_view, name="notification_page"),
]
