from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    context = {}
    return render(request, 'pages/layouts/profile.html', context)

def sessions(request):
    context = {}
    return render(request, 'pages/layouts/sessions.html', context)

def workshops(request):
    context = {}
    return render(request, 'pages/layouts/workshops.html', context)

def programs(request):
    context = {}
    return render(request, 'pages/layouts/programs.html', context)

def faq(request):
    context = {}
    return render(request, 'pages/layouts/faq.html', context)