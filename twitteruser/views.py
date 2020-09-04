from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import TwitterUserModel
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required
from notification import views



@login_required(login_url="login_page")
def index_view(request):
    tweets_by_login_user = Tweet.objects.filter(tweet_user=request.user).order_by('-created_at') 
    tweets_by_following_user = Tweet.objects.filter(tweet_user__in=request.user.following.all()).order_by('-created_at') 
    all_tweets = tweets_by_login_user | tweets_by_following_user
    total_tweets = Tweet.objects.filter(tweet_user__username=request.user.username).count() 
    noti_count = views.count_notification(request)
    return render(request,'index.htm',{'all_tweets':all_tweets,'total_tweets':total_tweets,'noti_count':noti_count})




def profile_view(request,user_name): 
    follow_flag = False      
    user_profile_data = TwitterUserModel.objects.get(username=user_name)   
    tweets = Tweet.objects.filter(tweet_user__username=user_name).order_by('-created_at')
    total_tweets = tweets.count() 
    if request.user.is_authenticated:    
        following_list = request.user.following.all()
    else:
        following_list = []


    if user_profile_data in following_list:
        follow_flag = True
    else:
        follow_flag = False
        
    context = {'tweets':tweets,'total_tweets':total_tweets,'user_profile_data':user_profile_data,'follow_flag':follow_flag}
    return render(request,'profile.htm',context)

def follow_view(request,user_name):    
    user_to_follow = TwitterUserModel.objects.get(username=user_name)
    login_user = TwitterUserModel.objects.get(username=request.user.username)
    login_user.following.add(user_to_follow)
    login_user.save() 
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def unfollow_view(request,user_name):    
    user_to_unfollow = TwitterUserModel.objects.get(username=user_name)
    login_user = TwitterUserModel.objects.get(username=request.user.username)
    login_user.following.remove(user_to_unfollow)
    login_user.save() 
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
