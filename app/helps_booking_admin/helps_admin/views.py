from datetime import datetime
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import generic
from django.utils.safestring import mark_safe


from dal import autocomplete

from helps_admin.models import StudentAccount, StaffAccount, Session
from helps_admin.cal import Calendar

# Create your views here.

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)


class CalendarView(generic.ListView):
    model = Session
    template_name = 'pages/layouts/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = datetime.today()

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['calendar_page'] = 'active'
        return context


def sessions(request):
    context = {'sessions_page': 'active', 'today': datetime.now().strftime('%Y-%m-%d'), 'min_hour': '9:00', 'max_hour': '17:00'}
    calendar = CalendarView.as_view()
    # use today's date for the calendar
    d = datetime.today()
    # Instantiate our calendar class with today's year and date
    cal = Calendar(d.day, d.year, d.month)
    # Call the formatmonth method, which returns our calendar as a table
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['calendar_page'] = 'active'
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

def message(request):
    context = {'message_page': 'active'}
    return render(request, 'pages/layouts/message.html', context)

def exit(request):
    logout(request)
    return redirect_view(request)

def redirect_view(request):
    response = redirect('/accounts/login/')
    return response

class StudentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return StudentAccount.objects.none()

        qs = StudentAccount.objects.all()

        if self.q:
            qs = qs.filter(student_id__istartswith=self.q)

        return qs

class StaffAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return StaffAccount.objects.none()

        qs = StaffAccount.objects.all()

        if self.q:
            qs = qs.filter(staff_id__istartswith=self.q)

        return qs

class CalendarView(generic.ListView):
    model = Session
    template_name = 'pages/layouts/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()