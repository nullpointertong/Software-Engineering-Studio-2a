"""helps_booking_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin, auth
from django.urls import path, include
from helps_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.generate_session_booking, name='sessions'),
    path('sessions/', views.generate_session_booking, name='sessions'),
    path('workshops/', views.workshops, name='workshops'),
    path('advisors/', views.advisors, name='advisors'),
    path('students/', views.students, name='students'),
    path('waiting_list/', views.waiting_list, name='waiting_list'),
    path('reports/', views.reports, name='reports'),
    path('template/', views.template, name='template'),
    path('email/', views.email, name='email'),
    path('room/', views.room, name='room'),
    path('messages/', views.messages, name='messages'),
    path('exit/', views.exit, name='exit'),
    path('search_sessions/', views.search_sessions, name='sessionlist')
]
