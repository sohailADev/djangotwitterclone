from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth import authenticate,login,logout
from . import forms
from twitteruser import models
# Create your views here.


def login_view(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data         
            user = authenticate(request, username=data.get('username'), password=data.get('password'))          
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("home_page")))
      
    form = forms.LoginForm()
    return render(request,'login.htm',{'form':form})
    # def login_view(request):
    # form = LoginForm(request.POST or None)
    # if request.POST and form.is_valid():
    #     user = form.login(request)
    #     if user:
    #         login(request, user)
    #         return HttpResponseRedirect("/n1.html")# Redirect to a success page.
    # return render(request, 'enter.html', {'login_form': form })

def signup_view(request):  
        if request.method == "POST":
            form = forms.SignUpForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data        
                signup_user = models.TwitterUserModel.objects.create_user(username = data.get('username'),password=data.get('password'),display_name=data.get('display_name'))
                if signup_user:                    
                    return HttpResponseRedirect(reverse("login_page"))           

        form = forms.SignUpForm()
        return render(request,"signup.htm",{'form':form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home_page"))