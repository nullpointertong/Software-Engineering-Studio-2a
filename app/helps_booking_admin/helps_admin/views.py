from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)

def sessions(request):
    context = {'sessions_page': 'active'}
    return render(request, 'pages/layout/sessions.html', context)

def workshops(request):
    context = {'workshops_page': 'active'}
    return render(request, 'pages/layout/workshops.html', context)

def advisors(request):
    context = {'advisors_page': 'active'}
    return render(request, 'pages/layout/advisors.html', context)

def students(request):
    context = {'students_page': 'active'}
    return render(request, 'pages/layout/students.html', context)

def waiting_list(request):
    context = {'waiting_list_page': 'active'}
    return render(request, 'pages/layout/waiting_list.html', context)

def reports(request):
    context = {'reports_page': 'active'}
    return render(request, 'pages/layout/reports.html', context)

def template(request):
    context = {'template_page': 'active'}
    return render(request, 'pages/layout/template.html', context)

def email(request):
    context = {'email_page': 'active'}
    return render(request, 'pages/layout/email.html', context)

def room(request):
    context = {'room_page': 'active'}
    return render(request, 'pages/layout/room.html', context)

def messages(request):
    context = {'messages_page': 'active'}
    return render(request, 'pages/layout/messages.html', context)

def exit(request):
    logout(request)
    return redirect_view(request)
