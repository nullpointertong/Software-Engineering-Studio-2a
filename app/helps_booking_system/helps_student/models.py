from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ungettext_lazy as _
from django.utils.translation import gettext_lazy as _g
from django.contrib.auth.models import User
from datetime import datetime

def parse_time_strings(time_string):
    '''Accepts a string and converts it into a list of datetimes'''
    result_list = []
    if len(time_string) != 19:
        raise ValidationError(_g('Invalid date/time, please format as: "DD-MM-YYYY HH:MM:SS"'))
    time_list = time_string.replace(' ','').split(',')
    for time_piece in time_list:
        day, month, year = time_piece[:10].split('-')
        hour, minute, second = time_piece[-8:].split(':')
        result_list.append(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second))
    return result_list

class SessionListField(models.Field):
    '''Field for list of sessions. Accepts list of datetimes'''

    description = _g('String of session times')

    def __init__(self, sessions=[], *args, **kwargs):
        self.sessions = sessions
        #self.max_length = 2048
        #kwargs['max_length'] = self.max_length 
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return ','.join([x.strftime('%d-%m-%Y %H:%M:%S') for x in self.sessions])

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Must return arguments to pass to __init__ for reconstruction
        if self.sessions != []:
            kwargs['sessions'] = self.sessions
        #del kwargs['max_length']
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'CharField'
    
    def rel_db_type(self, connection):
        return 'CharField'

    def get_prep_value(self, value):
        # Return comma separated string of datetimes
        return ','.join([x.strftime('%d-%m-%Y %H:%M:%S') for x in value])

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return parse_time_strings(value)

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        if value is None:
            return value
        return parse_time_strings(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)
    

class Session():
    session_ID = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(
        'StudentAccount',
        on_delete=models.CASCADE
    )
    staff_id = models.ForeignKey(
        'StaffAccount',
        on_delete=models.CASCADE
    )
    Location  = models.CharField(max_length=30)
    Session_time = models.DateTimeField()
    Has_Finished  = models.BooleanField()
    No_Show = models.BooleanField()

class StaffAccount():
    staff_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Email  = models.EmailField()
    # Session histories (Array of <Session>)
    # No-show history
    Faculty =  models.CharField(max_length=30)
    Course =  models.CharField(max_length=30)
    Preferred_First_Name = models.CharField(max_length=64)
    Phone = models.IntegerField()
    Mobile = models.IntegerField()
    Best_contact_no = models.IntegerField()
    DOB = models.DateField()
    Gender = models.CharField(max_length=24)
    Degree = models.CharField(max_length=64)
    Status = models.CharField(max_length=64)
    First_language = models.CharField(max_length=32)
    Country_of_origin = models.CharField(max_length=64)
    Educational_Background = models.CharField(max_length=64)

class StudentAccount():
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    Email  = models.EmailField()
    # Session histories (Array of <Session>)
    # No-show history
    Faculty =  models.CharField(max_length=32)
    Course =  models.CharField(max_length=64)
    Preferred_First_Name = models.CharField(max_length=64)
    Phone = models.IntegerField()
    Mobile = models.IntegerField()
    Best_contact_no = models.IntegerField()
    DOB = models.EmailField()
    Gender = models.CharField(max_length=32)
    Degree = models.CharField(max_length=64)
    Status = models.CharField(max_length=64)
    First_language = models.CharField(max_length=32)
    Country_of_origin = models.CharField(max_length=30)
    Educational_Background = models.CharField(max_length=30)



# class UserAccount(models.Model):
#     user = models.ForeignKey(User)
#     first_name = models.CharField()
#     last_name = models.CharField()

#     def __str__(self):
#         return self.first_name + " " + self.last_name


# class Session(models.Model):
#     student = models.ForeignKey(UserAccount)
#     advisor = models.ForeignKey(UserAccount)
#     session_time = models.DateTimeField('Session Time')
#     venue = models.CharField('Location', max_length=20)





