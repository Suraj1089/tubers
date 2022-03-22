from distutils.command.upload import upload
from email.policy import default
from enum import auto
from pyexpat import model
from venv import create
from django.db import models

# Create your models here.

class Slider(models.Model):
    # blank = True means we can kept it empty 
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider/%Y/') #upload image to given path %y means year wise floder
    created_date = models.DateTimeField(auto_now_add=True)
    external_link = models.CharField(max_length=500,default=True)
    
    
    def __str__(self):
        return self.headline
    
    
class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateField(auto_now_add=True)
    you_tube_link = models.URLField(default=True, max_length=1000)
    
    
    
    def __str__(self):
        return self.first_name