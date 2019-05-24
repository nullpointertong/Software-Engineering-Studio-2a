import calendar
from datetime import *
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.views import generic
from django.utils.safestring import mark_safe
from django.utils import timezone

from dal import autocomplete

from helps_admin.models import Session, StudentAccount, StaffAccount
from helps_admin.cal import Calendar
from .forms import StudentForm, StaffForm, CreateSessionForm

from .forms import BookSessionForm
from .models import StudentAccount, StaffAccount, Session

# Create your views here.

def user_is_valid(_user):
    """Accepts (Student/Staff)Accounts and checks if all are in the databse."""
    # TODO: Validate user in database
    if isinstance(_user, StudentAccount) or isinstance(_user, StaffAccount):
        return _user in StudentAccount.objects.all() and _user in StaffAccount.objects.all()
    elif isinstance(_user, list):
        # Large impact database lookup, use singular validation if possible
        for user in _user:
            if user not in StudentAccount.objects.all() and user not in StaffAccount.objects.all():
                return False
        return True

def search_sessions(request):
    # Process request
    if request.method == "POST":
        # Unpack and validate
        data = request.POST
        # TODO: 
        students = StudentAccount.objects.filter(
            student_id__contains=data["student_id"],
            first_name__contains=data["first_name"],
            last_name__contains=data["last_name"],
        )
        sessions = Session.objects.filter(
            date__contains=data["date"]
        )        

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


def create_session(request):
    if request.method == "POST":
        data = request.POST
        context = {}
        context['errors'] = []
        context['form_valid'] = True
        context['time_selection_visible'] = 'block'
        # print(data)
        # Session date
        today = date.today()
        date_ = data['req_sess_date']
        context['default_date'] = date_
        y, m, d = map(int, date_.split('-'))
        if date(y, m, d) < today:
            context['form_valid'] = False
            context['errors'] += 'Date cannot be in the past!',
        # Starting hour, minute, am/pm
        sh, sm = data['req_sess_sh'], data['req_sess_sm']
        # Ending hour, minute, am/pm
        eh, em = data['req_sess_eh'], data['req_sess_em']
        hour_options = SessionView.opt_hours.replace("value='%s'" % sh, "value='%s' selected='selected'" % sh) # Set default as the selected value
        minute_options = SessionView.opt_minutes.replace("value='%s'" % sm, "value='%s' selected='selected'" % sm)
        hour_options_1 = SessionView.opt_hours.replace("value='%s'" % eh, "value='%s' selected='selected'" % eh)
        minute_options_1 = SessionView.opt_minutes.replace("value='%s'" % em, "value='%s' selected='selected'" % em)
        context.update(
            {
                'opt_hours': mark_safe(hour_options),
                'opt_minutes': mark_safe(minute_options),
                'opt_hours_1': mark_safe(hour_options_1),
                'opt_minutes_1': mark_safe(minute_options_1)
            }
        )
        selected_date = date(y, m, d)
        context['prev_month'] = prev_month(selected_date)
        context['next_month'] = next_month(selected_date)

        context['default_location'] = data['req_location']
        
        student_query = data['req_student_id']
        advisor_query = data['req_advisor_id']

        if student_query.isdigit():
            matched_student = StudentAccount.objects.filter(student_id__exact=student_query)
            if len(matched_student) == 0:
                context['form_valid'] = False
                context['student_info'] = "NOT FOUND"
                context['student_info_color'] = "color: red"
                context['errors'] += 'Student ID not registered with HELPS.',
            else:
                context['student_info'] = matched_student[0].last_name.upper() + ', ' + matched_student[0].first_name
        else:
            context['form_valid'] = False
            context['student_info'] = "INVALID INPUT"
            context['student_info_color'] = "color: red"
            context['errors'] += 'Student ID must be numerical.',

        if advisor_query.isdigit():
            matched_advisor = StaffAccount.objects.filter(staff_id__exact=advisor_query)
            if len(matched_advisor) == 0:
                context['form_valid'] = False
                context['advisor_info'] = "NOT FOUND"
                context['advisor_info_color'] = "color: red"
                context['errors'] += 'Advisor ID not registered with HELPS.',
            else:
                context['advisor_info'] = matched_advisor[0].last_name.upper() + ', ' + matched_advisor[0].first_name
        else:
            context['form_valid'] = False
            context['advisor_info'] = "INVALID INPUT"
            context['advisor_info_color'] = "color: red"
            context['errors'] += 'Staff ID must be numerical.',

        context['default_student'] = student_query
        context['default_advisor'] = advisor_query
        context['clean_page'] = False

        if data['confirm_booking'] == 'yes':
            start_time = datetime(y, m, d, int(sh), int(sm), tzinfo=timezone.utc)
            end_time = datetime(y, m, d, int(eh), int(em), tzinfo=timezone.utc)
            Session.objects.create(
                student=matched_student[0],
                staff=matched_advisor[0],
                start_time=start_time, # This is starting time, still missing end time
                end_time=end_time,
                location=context['default_location'],
                has_finished=False,
                no_show=False,)
            context['from_time'] = start_time
            context['to_time'] = end_time
            return render(request, 'pages/layouts/session_booked.html', context)
        else:
            context['page_title'] = 'Confirm Booking' if context['form_valid'] else 'Book a Session'
            context['calendar'] = mark_safe(SessionView.calendar.new_date(y, m, d).formatmonth(True, context['prev_month'], context['next_month']))
            return render(request, 'pages/layouts/create_session.html', context)
    elif request.method == "GET":
        d = get_date(request.GET.get('month', None))
        # Instantiate our calendar class with the selected day's year and date
        cal = SessionView.calendar.new_date(d.year, d.month, d.day)

        return SessionView.as_view()(request, {'calendar': cal})
            

class SessionView(generic.ListView):
    model = Session
    template_name = 'pages/layouts/create_session.html'
    form = CreateSessionForm()
    # Drop down options for hours and minutes
    opt_hours = '\n'.join(["<option value='{0:02d}'>{0:02d}</option>".format(i) for i in range(7, 21)])
    opt_minutes = '\n'.join(["<option value='{0:02d}'>{0:02d}</option>".format(i) for i in range(0, 60, 15)])
    today = datetime.today()
    calendar = Calendar(today.year, today.month, today.day)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'page_title': 'Book a Session',
            'default_date': datetime.now().strftime('%Y-%m-%d'),
            'default_student': '',
            'default_advisor': '',
            'default_location': '',
            'opt_hours': mark_safe(SessionView.opt_hours),
            'opt_minutes': mark_safe(SessionView.opt_minutes),
            'opt_hours_1': mark_safe(SessionView.opt_hours),
            'opt_minutes_1': mark_safe(SessionView.opt_minutes),
            'time_selection_visible': 'none',
            'clean_page': True,
            'form_valid': False,
            'student_info': '',
            'advisor_info': ''
        })
        d = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with the selected day's year and date
        cal = SessionView.calendar.new_date(d.year, d.month, d.day)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        # print (context)
        html_cal = cal.formatmonth(True, context['prev_month'], context['next_month'])

        context['calendar'] = mark_safe(html_cal)
        context['form'] = SessionView.form

        return context


def sessions(request):
    return render(request, 'pages/layouts/sessions.html')

def get_date(req_day):
    if req_day:
        date_elems = [int(x) for x in req_day.split('-')]
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


