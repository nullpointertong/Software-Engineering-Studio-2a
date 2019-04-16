from django import forms


class StudentForm(forms.Form):
    DOB = forms.DateField(help_text="Enter")

#Expermenting with the forms.py fucntionality