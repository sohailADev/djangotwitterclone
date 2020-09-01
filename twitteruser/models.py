from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class TwitterUserModel(AbstractUser):
    display_name = models.CharField(max_length=40,null=True,blank=True)
    following = models.ManyToManyField("self", symmetrical=False)
    
    # dob
    # image
    # info

    def __str__(self):
        return self.username
