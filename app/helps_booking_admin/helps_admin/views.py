from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

from .forms import BookSessionForm

# Create your views here.

def user_is_valid(_user):
    """Accepts list or user string"""
    # TODO: Validate user in database
    return True

def generate_session_booking(request):
    # Process POST request
    if request.method == "POST":
        # Generate form instance from request data
        book_session_form = BookSessionForm(request.POST)
        # Process form if it is valid
        if book_session_form.is_valid():
            session_instance = book_session_form.save(commit=False)
            # TODO: Add student and staff by looking up in the database. Abort if users are not valid.
            if not user_is_valid([session_instance.student, session_instance.staff]):
                # TODO raise error
                pass
            session_instance.save()
            return HttpResponseRedirect("sessions") # redirect TODO: Edit redirect
    else:
        book_session_form = BookSessionForm()
    context = {
        "book_session_form": book_session_form
    }
    return render(request, 'pages/layouts/sessions.html', context)

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)

def sessions(request):
    context = {'sessions_page': 'active', 'today': datetime.now().strftime('%Y-%m-%d'), 'min_hour': '9:00', 'max_hour': '17:00'}
    
    return render(request, 'pages/layouts/sessions.html', context)

def workshops(request):
    context = {'workshops_page': 'active'}
    return render(request, 'pages/layouts/workshops.html', context)

def advisors(request):
    context = {'advisors_page': 'active'}
    return render(request, 'pages/layouts/advisors.html', context)

def students(request):
    context = {'students_page': 'active'}
    return render(request, 'pages/layouts/students.html', context)

def waiting_list(request):
    context = {'waiting_list_page': 'active'}
    return render(request, 'pages/layouts/waiting_list.html', context)

def reports(request):
    context = {'reports_page': 'active'}
    return render(request, 'pages/layouts/reports.html', context)

def template(request):
    context = {'template_page': 'active'}
    return render(request, 'pages/layouts/template.html', context)

def email(request):
    context = {'email_page': 'active'}
    return render(request, 'pages/layouts/email.html', context)

def room(request):
    context = {'room_page': 'active'}
    return render(request, 'pages/layouts/room.html', context)

def messages(request):
    context = {'messages_page': 'active'}
    return render(request, 'pages/layouts/messages.html', context)

def exit(request):
    logout(request)
    return redirect_view(request)

def redirect_view(request):
    response = redirect('/accounts/login/')
    return response


