from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from notification.models import Notification
# Create your views here.

@login_required(login_url="login_page")
def notification_view(request):
    notifications = Notification.objects.filter(user_to_notify=request.user)
    noti_count = 0
    new_notification = []
    for notification in notifications:
        if notification.notification_flag == False:
            noti_count +=1
            new_notification.append(notification.tweet_to_be_notify)
            notification.notification_flag = True
            notification.save() 

    return render(request,'notification.htm',{'new_notification':new_notification,'noti_count':noti_count})



def count_notification(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user_to_notify=request.user)
        noti_count = 0  
        for notification in notifications:
            if notification.notification_flag == False:
                noti_count += 1
    else:
        noti_count = 0  

    return noti_count 
           

