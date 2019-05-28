from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import StudentAccount
from .forms import StudentForm

def login_request(request):
    context = {'login_request': 'active'}
    return render(request, 'registration/login.html', context)

def profile(request):
    context = {'profile_page': 'active'}
    return render(request, 'pages/layouts/profile.html', context)

def submit_profile(request):
    print("DEBUG FORM ADDED")
    #Debug message
    #SQL Query to retrieve current Student ID - temp field:
    student_id = request.POST["student_id"]
    #Retrieve Information from HTML
    student_first_name = request.POST["student_first_name"]
    student_last_name = request.POST["student_last_name"]
    student_preferred_first_name = request.POST["student_preferred_first_name"]
    student_preferred_last_name = request.POST["student_preferred_last_name"]
    student_faculty = request.POST["student_faculty"]
    student_course = request.POST["student_course"]
    student_email = request.POST["student_email"]
    student_home_phone = request.POST["student_home_phone"]
    student_mobile = request.POST["student_mobile"]
    student_best_contactno = request.POST["student_best_contactno"]
    student_DOB = request.POST["student_DOB"]
    student_gender = request.POST["student_gender"]
    student_degree = request.POST["student_degree"]
    #student_year = request.POST["student_year"]
    student_status = request.POST["student_status"]
    student_language = request.POST["student_language"]
    student_country = request.POST["student_country"]
    #student_name = request.POST["student_name"]
    student_account = StudentAccount(
        #Piping Infomration into Model
        student_id = student_id,
        first_name = student_first_name,
        last_name = student_last_name,
        email = student_email,
        faculty =  student_faculty,
        course =  student_course,
        preferred_first_name = student_preferred_first_name,
        preferred_last_name = student_preferred_last_name,
        phone = student_home_phone,
        mobile = student_mobile,
        best_contact_no = student_best_contactno,
        DOB = student_DOB,
        gender = student_gender,
        degree = student_degree,
        status = student_status,
        first_language = student_language,
        country_of_origin = student_country

    # Needs to be made into an array educational_background = models.CharField(max_length=30)
    )
    student_account.save()
    context = {'profile_page': 'active'}
    return render(request,'pages/layouts/profile.html', context)

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

# def get_request(self, request):
#     form = StudentForm() 
#     return render(request,self.template_name,{'form':form})
# Just playing around with form rendering from a forms.py file.

def exit(request):
    logout(request)
    return redirect_view(request)

def redirect_view(request):
    response = redirect('/accounts/login/')
    return response




# def some_name(request):
#     foo_instance = Foo.objects.create(name='test')
#     return render(request, 'some_name.html.html')

# def send(request): 
#     publisher_instance = Publisher.objects.create(name='tux') 
#     return HttpResponse("done")

# fruit = Fruit.objects.create(name='Apple')
# >>> fruit.name = 'Pear'
# >>> fruit.save()
# >>> Fruit.objects.values_list('name', flat=True)