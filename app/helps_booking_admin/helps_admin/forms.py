import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class BookSessionForm(forms.Form):
    field_student_no = forms.UUIDField(help_text="Enter student ID of the student")
    field_advisor_no = forms.UUIDField(help_text="Enter staff ID of the advisor")
    # TODO: Search option to search for staff
    field_date = forms.DateField(help_text="Select a date for the session.")

    field_start_time = forms.TimeField(help_text="Select the time when the session starts")
    field_end_time = forms.TimeField(help_text="Select the time when the session ends")

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
