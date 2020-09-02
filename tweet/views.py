from . import forms
from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from . import models


# Create your views here.
def tweet_view(request):
    return render(request,'tweet.htm',{})

def add_tweet_view(request):      
    form = forms.AddTweetForm(request.POST or None)
    if request.POST and form.is_valid():
        data = form.cleaned_data
        new_tweet = models.Tweet.objects.create(tweet_content = data['tweet_content'],tweet_user=request.user)
        if new_tweet:            
            return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
  
    return render(request,'addtweet.htm',{'form':form})


def tweet_detail_view(request,tweet_id):   
    tweets = models.Tweet.objects.filter(id=tweet_id)
    total_tweets = models.Tweet.objects.filter(tweet_user__username=request.user.username).count()  
    return render(request,'index.htm',{'tweets':tweets,'total_tweets':total_tweets})

