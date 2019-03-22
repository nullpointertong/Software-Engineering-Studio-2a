from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    context = {'profile_page': 'active'}
    return render(request, 'pages/layouts/profile.html', context)

def sessions(request):
    context = {'sessions_page': 'active'}
    return render(request, 'pages/layouts/sessions.html', context)

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
