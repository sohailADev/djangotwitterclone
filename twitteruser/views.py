from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import TwitterUserModel
from tweet.models import Tweet
from django.contrib.auth.decorators import login_required




@login_required(login_url="login_page")
def index_view(request):
    tweets = Tweet.objects.all().order_by('-created_at') 
    total_tweets = Tweet.objects.filter(tweet_user__username=request.user.username).count() 
    return render(request,'index.htm',{'tweets':tweets,'total_tweets':total_tweets})




def profile_view(request,user_name):   
    tweets = Tweet.objects.filter(tweet_user__username=user_name).order_by('-created_at')
    total_tweets = tweets.count() 
    return render(request,'index.htm',{'tweets':tweets,'total_tweets':total_tweets})

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
