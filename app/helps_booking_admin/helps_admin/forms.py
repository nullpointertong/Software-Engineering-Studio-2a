from django import forms
from .models import Session, StaffAccount, StudentAccount

class MultipleForm(forms.Form):
    pass

class BookSessionForm(forms.ModelForm):
    """Post a form to create a new session"""
    class Meta:
        model = Session
        fields = ["location", "student", "staff", "start_time", "end_time",]
    date = forms.DateField(label="Date:")
    start_time = forms.TimeField(label="Start time:")
    end_time = forms.TimeField(label="End time:")
    location = forms.CharField(label="Room:", max_length=30)
    # student and advisor should be an automatically filtered list
    student = forms.CharField(label="Full student name:", max_length=255)
    staff = forms.CharField(label="Full advisor name:", max_length=255)
    
class ViewSessionForm(forms.Form):
    """View current existing sessions from database"""
    pass