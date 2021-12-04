"""hotelmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotel.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signuppage),
    path('login/', login),
    path('',default,name="default"),
    path('logout/', logout),
    path('aboutus/',aboutus),
    path('banquet/',banquet),
    path('contact/',contact),
    path('feedback/',feedback),
    path('masalagrill/',MASALAGRILL),
    path('roomgallery/',roomgallery),
    path('roomgallery/',room),
    path('roomtraffi/',roomtraffi),
    path('skybar/',skybar),
    path('theloop/',theloop),
    path('booking/',roombooking),
    path('roomdetail/',roomdetail),
    path('userabout/',userabout),
    path('userhelp/',userhelp),
    path('baseprofile/',baseprofile),
    path('displayroom/',displayroom),
    path('editprofile/',editprofile),
    path('menu/',menuview),
    path('userpassword/',userpassword),
    path('maintemplate/',maintemplate),
    path('menudata/',menudata),
    path('checkAva/',checkAva),
    path('bookhistory/<str:ttime>',bookinghistory),
    path('roompayment/',roompayment),
    path('checkout/',checkout),
    # path('success/<str:time>', success_view)
    ]

if settings.DEBUG:
    urlpatterns +=staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
