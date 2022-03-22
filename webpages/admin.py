from re import search
from django.contrib import admin
from . models import Slider, Team
# Register your models here.
from django.utils.html import format_html
class TeamAdmin(admin.ModelAdmin):#this clas is for admin panel 
    
    def myphoto(self,object):
        return format_html('<img src="{}"width="40"'.format(object.photo.url))
        
    list_display = ('id','myphoto','first_name','role','created_date')#these values display below team
    list_display_link = ('id','role')
    search_fields = ('first_name','role')
    list_filter = ('role',)
    
admin.site.register(Team,TeamAdmin)
admin.site.register(Slider) #registering slider class to admin panel so we can access it 