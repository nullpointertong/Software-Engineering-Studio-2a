from django.contrib import admin

# Register your models here.
# from .forms import StudentsForm
from .models import StudentAccount, StaffAccount, Session, Workshop

# class StudentAdmin(admin.ModelAdmin):
#     form = StudentsForm

admin.site.register(StudentAccount)
admin.site.register(StaffAccount)
admin.site.register(Session)
admin.site.register(Workshop)