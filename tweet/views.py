from . import forms
from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from . import models
from twitteruser.models import TwitterUserModel
from notification.models import Notification
import re
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from  django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def tweet_view(request):
    return render(request,'tweet.htm',{})


    
# @login_required(login_url="login_page")
# def add_tweet_view(request):      
#     form = forms.AddTweetForm(request.POST or None)
#     if request.POST and form.is_valid():
#         data = form.cleaned_data
#         new_tweet = models.Tweet.objects.create(tweet_content = data['tweet_content'],tweet_user=request.user)
#         # regex to extract username  
#         mentions = re.findall(r'@(\w+)', data['tweet_content'])
#         # IF REGEX IS TRUE 
#         if mentions:
#             for mention in mentions:
#                 matched_user = TwitterUserModel.objects.get(username=mention)
#                 if matched_user:                    
#                     # CRETE  NEW NOTIFICATION 
#                     Notification.objects.create( 
#                     user_to_notify = matched_user,
#                     tweet_to_be_notify = new_tweet
#                 )

#         if new_tweet:            
#             return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
  
#     return render(request,'addtweet.htm',{'form':form})

class AddTweetView(LoginRequiredMixin,TemplateView):
    def get(self,request):
        form = forms.AddTweetForm()
        return render(request,'addtweet.htm',{'form':form})
    def post(self,request):      
        form = forms.AddTweetForm(request.POST)
        if request.POST and form.is_valid():
            data = form.cleaned_data
            new_tweet = models.Tweet.objects.create(tweet_content = data['tweet_content'],tweet_user=request.user)
            # regex to extract username  
            mentions = re.findall(r'@(\w+)', data['tweet_content'])
            # IF REGEX IS TRUE 
            if mentions:
                for mention in mentions:
                    matched_user = TwitterUserModel.objects.get(username=mention)
                    if matched_user:                    
                        # CRETE  NEW NOTIFICATION 
                        Notification.objects.create( 
                        user_to_notify = matched_user,
                        tweet_to_be_notify = new_tweet
                    )

            if new_tweet:            
                return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
        form = forms.AddTweetForm()
        return render(request,'addtweet.htm',{'form':form})
class TweetDetailView(LoginRequiredMixin,TemplateView):
    def get(self,request,tweet_id):
        tweets = models.Tweet.objects.get(id=tweet_id)     
        return render(request,'tweetdetail.htm',{'tweet':tweets})