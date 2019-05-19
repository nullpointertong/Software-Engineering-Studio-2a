import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import widgets
from dal import autocomplete

from helps_admin.models import StudentAccount, StaffAccount

class CreateSessionForm(forms.Form):
    field_student_id = forms.UUIDField(help_text="Student ID")
    field_advisor_id = forms.UUIDField(help_text="Advisor Staff ID")
    field_date = forms.DateField(help_text="Session date")
    field_start_time = forms.TimeField(help_text="From")
    field_end_time = forms.TimeField(help_text="To")
    field_notes = forms.CharField(widget=forms.Textarea, help_text="Notes")

    def clean_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date'))

        # Check if a date is in the allowed range (+4 weeks from today).
        # if data > datetime.date.today() + datetime.timedelta(weeks=4):
        #     raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentAccount
        fields = ('__all__')
        widgets = {
            'student': autocomplete.ModelSelect2(
                url='student-autocomplete',
                attrs={
                    'data-placeholder': 'Enter name or student ID...'
                }
            )
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = StaffAccount
        fields = ('__all__')
        widgets = {
            'staff': autocomplete.ModelSelect2(
                url='staff-autocomplete',
                attrs={
                    'data-placeholder': 'Enter name or staff ID...',
                }
            )
        }