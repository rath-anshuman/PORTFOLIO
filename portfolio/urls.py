
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf import settings
# from django.conf.urls import url
from django.conf.urls.static import static

import  portfolio.views  as mainview 

import contactme.views as cntviews
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('pwa.urls')),
    path('', mainview.home,name='home'),
    
    path('sayhi', cntviews.hipage,name='sayhi'),
    path('contactme', cntviews.contactme,name='contactme'),
] 
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
