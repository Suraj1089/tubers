from datetime import datetime
from venv import create
from django.db import models

# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    state = models.CharField(max_length=13)
    message = models.TextField(max_length=13)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default=datetime.now)
    
    
    def __str__(self):
        return self.email