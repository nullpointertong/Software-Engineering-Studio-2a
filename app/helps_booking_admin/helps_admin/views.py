import calendar
from datetime import *
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import generic
from django.utils.safestring import mark_safe

from dal import autocomplete

from helps_admin.models import Session, StudentAccount, StaffAccount
from helps_admin.cal import Calendar
from helps_admin.forms import StudentForm, StaffForm, CreateSessionForm

# Create your views here.

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)


def create_session(request):
    if request.method == "POST":
        session_valid = True
        context = {}
        context['time_selection_visible'] = 'block'
        today = date.today()
        context['today'] = today.strftime("%Y-%m-%d")
        data = request.POST
        # print(data)
        # Session date
        date_ = data['req_sess_date']
        context['default_date'] = date_
        y, m, d = map(int, date_.split('-'))
        if date(y, m, d) < today:
            session_valid = False
            context['err_date_past'] = True
        # Starting hour, minute, am/pm
        sh, sm, sa = data['req_sess_sh'], data['req_sess_sm'], data['req_sess_sa']
        # Ending hour, minute, am/pm
        eh, em, ea = data['req_sess_eh'], data['req_sess_em'], data['req_sess_ea']
        context.update(
            {
                'opt_hours': SessionView.opt_hours,
                'opt_minutes': SessionView.opt_minutes,
                'opt_am_pm': SessionView.opt_am_pm,
            }
        )
        start_time = time(int(sh) % 12 if sa == 'AM' else int(sh) % 12 + 12, int(sm))
        end_time = time(int(eh) % 12 if ea == 'AM' else int(eh) % 12 + 12, int(em))
        selected_date = date(y, m, d)
        context['prev_month'] = prev_month(selected_date)
        context['next_month'] = next_month(selected_date)
        
        student_query = data['req_student_id']
        advisor_query = data['req_advisor_id']

        matched = StudentAccount.objects.filter(student_id__exact=student_query)
        if len(matched) == 0:
            session_valid = False
            context['err_student'] = True
        else:
            context['student_info'] = matched[0]
        matched = StaffAccount.objects.filter(staff_id__exact=advisor_query)
        if len(matched) == 0:
            session_valid = False
            context['err_advisor'] = True
        else:
            context['advisor_info'] = matched[0]
        context['default_student'] = student_query
        context['default_advisor'] = advisor_query
        context['page_mode'] = 'confirm'
        context['book_button_ready'] = session_valid

        context['calendar'] = mark_safe(SessionView.calendar.new_date(y, m, d).formatmonth(True, context['prev_month'], context['next_month']))
        return render(request, 'pages/layouts/sessions.html', context)
            

class SessionView(generic.ListView):
    model = Session
    template_name = 'pages/layouts/sessions.html'
    form = CreateSessionForm()
    opt_hours = mark_safe('\n'.join(["<option value='{0:02d}'>{0:02d}</option>".format(i) for i in range(1, 13)]))
    opt_minutes = mark_safe('\n'.join(["<option value='{0:02d}'>{0:02d}</option>".format(i) for i in range(0, 60, 15)]))
    opt_am_pm = mark_safe('\n'.join(["<option value='{0}'>{0}</option>".format(i) for i in ['AM', 'PM']]))
    today = datetime.today()
    calendar = Calendar(today.year, today.month, today.day)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sessions_page': 'active',
            'today': datetime.now().strftime('%Y-%m-%d'),
            'default_student': '',
            'default_advisor': '',
            'opt_hours': SessionView.opt_hours,
            'opt_minutes': SessionView.opt_minutes,
            'opt_am_pm': SessionView.opt_am_pm,
            'time_selection_visible': 'none',
            'page_mode': 'start',
            'err_date_past': False,
            'err_student': False,
            'err_advisor': False,
            'student_info': None,
            'advisor_info': None,
            'book_button_ready': False
        })
        d = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with the selected day's year and date
        cal = SessionView.calendar.new_date(d.year, d.month, d.day)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        print (context)
        html_cal = cal.formatmonth(True, context['prev_month'], context['next_month'])

        context['calendar'] = mark_safe(html_cal)
        context['form'] = SessionView.form

        return context

def get_date(req_day):
    if req_day:
        date_elems = (int(x) for x in req_day.split('-'))
        if len(date_elems) == 2:
            year, month = date_elems
        elif len(date_elems) == 3:
            year, month, _ = date_elems
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


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
