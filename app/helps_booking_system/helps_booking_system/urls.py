"""helps_booking_system URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from helps_student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.redirect_view, name='Login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/submit_profile/', views.submit_profile, name='submit_profile'),
    path('workshops/', views.workshops, name='workshops'),
    path('bookings/', views.bookings, name='bookings'),
    path('programs/', views.programs, name='programs'),
    path('faq/', views.faq, name='faq'),
    path('exit/', views.exit, name='exit')
]

