from django.shortcuts import render,redirect
from django.http import HttpResponse

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)

def profile(request):
    context = {'profile_page': 'active'}
    return render(request, 'pages/layouts/profile.html', context)

def bookings(request):
    context = {'booking_page': 'active'}
    return render(request, 'pages/layouts/booking.html', context)

def workshops(request):
    context = {'workshops_page': 'active'}
    return render(request, 'pages/layouts/workshops.html', context)

def programs(request):
    context = {'programs_page': 'active'}
    return render(request, 'pages/layouts/programs.html', context)

def faq(request):
    context = {'faq_page': 'active'}
    return render(request, 'pages/layouts/faq.html', context)

def exit(request):
    context = {}
    return render(request, 'pages/layouts/profile.html', context)

def redirect_view(request):
    response = redirect('accounts/login/')
    return response
