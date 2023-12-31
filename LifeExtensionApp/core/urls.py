"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from COMMON_APP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home Page
    path('', home , name = 'home' ),
    path('register', register , name = 'register' ),
    path('login', login , name = 'login' ),
    path('logout', logout , name = 'logout' ),
    path('feedback', feedback, name = 'feedback' ),
    path('profile/(?P<user>.*)/$', profile , name = 'profile' ),
    path('dashboard/(?P<user>.*)/$', dashboard , name = 'dashboard'),
    path('create_appointment/(?P<user>.*)/$', create_appointment , name = 'create_appointment'),
    path('delete_patient/(?P<id>\d+)/$', delete_patient , name = 'delete_patient'),
    path('myappointment/', myappointment , name = 'myappointment'),
    path('docter_appointment/', docter_appointment , name = 'docter_appointment'),
    path('docter_prescription/', docter_prescription , name = 'docter_prescription'),
    path('room_reservation/', room_reservation , name = 'room_reservation'),
    path('reserved_rooms/', reserved_rooms , name = 'reserved_rooms'),
    path('create_prescription/', create_prescription , name = 'create_prescription'),
    path('medical_history/', medical_history , name = 'medical_history'),
    path('update_docter/(?P<id>\d+)/$', update_docter , name = 'update_docter'),
    path('send_confirmation/(?P<id>\d+)/$', send_confirmation , name = 'send_confirmation'),
    








    










]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)


