from django.shortcuts import render
from django.http import HttpResponse

def profile(request, username="user"):
    return HttpResponse('Hello, {}!'.format(username))
