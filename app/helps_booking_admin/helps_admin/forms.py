from django import forms
from .models import Session, StaffAccount, StudentAccount

class BookSessionForm(forms.ModelForm):
    """Post a form to create a new session"""
    datetime_formats = [
        "%d-%m-%Y %H:%M:%S" #25-12-2019 14:40:35
    ]
    start_time = forms.DateTimeField(label="Start Time (DD-MM-YYYY HH:MM:SS)", required=True, input_formats=datetime_formats)
    end_time = forms.DateTimeField(label="End Time (DD-MM-YYYY HH:MM:SS)", required=True, input_formats=datetime_formats)
    class Meta:
        model = Session
        fields = ["location", "student", "staff"]
    # date = forms.DateField(label="Date:")
    # start_time = forms.TimeField(label="Start time:")
    # end_time = forms.TimeField(label="End time:")
    # location = forms.CharField(label="Room:", max_length=30)
    # # student and advisor should be an automatically filtered list
    # student = forms.CharField(label="Full student name:", max_length=255)
    # staff = forms.CharField(label="Full advisor name:", max_length=255)
