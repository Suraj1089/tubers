from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webpages.urls')),
    path('hiretubers/',include('hiretubers.urls')),
    path('youtubers/',include('youtubers.urls')),
    path('accounts/',include('accounts.urls')),
    path('socialaccounts/',include('allauth.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
                