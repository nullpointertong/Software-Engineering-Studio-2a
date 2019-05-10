from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ungettext_lazy as _
from django.utils.translation import gettext_lazy as _g
from django.contrib.auth.models import User
from datetime import datetime

def parse_time_strings(time_string):
    '''Accepts comma separated string of datetimes and converts it into a list of datetimes'''
    result_list = []
    if time_string == "":
        return None
    time_list = time_string.replace(' ','').split(',')
    for time_piece in time_list:
        if len(time_piece) != 18:
            raise ValidationError(_g('Invalid date/time, please format as: "DD-MM-YYYY HH:MM:SS"'))
        day, month, year = [int(x) for x in time_piece[:10].split('-')]
        hour, minute, second = [int(x) for x in time_piece[-8:].split(':')]
        result_list.append(datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second))
    return result_list

class DateListField(models.Field):
    '''Field for multiple dates. Accepts list of datetimes'''

    description = _g('String of datetimes')

    def __init__(self, dates=[], *args, **kwargs):
        self.dates = dates
        #self.max_length = 2048
        #kwargs['max_length'] = self.max_length 
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        return ','.join([x.strftime('%d-%m-%Y %H:%M:%S') for x in self.dates])

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Must return arguments to pass to __init__ for reconstruction
        if self.dates != []:
            kwargs['dates'] = self.dates
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
    

class Session(models.Model):

    session_ID = models.IntegerField(primary_key=True, unique=True)
    # One StudentAccount has many Sessions
    student = models.ForeignKey(
        'StudentAccount',
        on_delete=models.CASCADE
    )
    # One StaffAccount has many Sessions
    staff = models.ForeignKey(
        'StaffAccount',
        on_delete=models.CASCADE
    )
    location  = models.CharField(max_length=30)
    session_time = models.DateTimeField()
    has_finished  = models.BooleanField()
    no_show = models.BooleanField()

    def __str__(self):
        return "\n".join([
            "Session ID: {}".format(self.session_ID),
            "Staff: {}".format(self.staff),
            "Student: {}".format(self.student)
        ])

class Workshop(models.Model):

    workshop_ID = models.IntegerField(primary_key=True, unique=True)
    # One StaffAccount has many Workshops
    staff = models.ForeignKey(
        'StaffAccount',
        on_delete=models.CASCADE
    )
    # Many StudentAccounts have many Workshops
    students = models.ManyToManyField('StudentAccount')
    max_students = models.PositiveIntegerField()
    skill_set_name = models.CharField(max_length=64)
    start_dates = DateListField()
    end_dates = DateListField()
    room = models.CharField(max_length=32)

    def __str__(self):
        return "\n".join([
            "Workshop ID: {}".format(self.workshop_ID),
            "Staff: {}".format(self.staff),
            "Students: {}".format(self.students)
        ])
        

class StaffAccount(models.Model):

    staff_id = models.PositiveIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email  = models.EmailField()
    session_history = DateListField()
    #no_show_history = DateListField()
    faculty =  models.CharField(max_length=30)
    course =  models.CharField(max_length=30)
    preferred_first_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    best_contact_no = models.CharField(max_length=12)
    DOB = models.DateField()
    gender = models.CharField(max_length=24)
    degree = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    first_language = models.CharField(max_length=32)
    country_of_origin = models.CharField(max_length=64)
    educational_background = models.CharField(max_length=64)

    def __str__(self):
        return 'ID: {} - {}{}{}'.format(
            self.staff_id,
            self.first_name,
            " (Pref: " + self.preferred_first_name + ") " if self.preferred_first_name != "" else " ",
            self.last_name
        )

class StudentAccount(models.Model):

    student_id = models.PositiveIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    session_history = DateListField()
    no_show_history = DateListField()
    faculty =  models.CharField(max_length=32)
    course =  models.CharField(max_length=64)
    preferred_first_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    best_contact_no = models.CharField(max_length=12)
    DOB = models.EmailField()
    gender = models.CharField(max_length=32)
    degree = models.CharField(max_length=64)
    status = models.CharField(max_length=64)
    first_language = models.CharField(max_length=32)
    country_of_origin = models.CharField(max_length=30)
    educational_background = models.CharField(max_length=30)
    

    def __str__(self):
        return 'ID: {} - {}{}{}'.format(
            self.student_id,
            self.first_name,
            " (Pref: " + self.preferred_first_name + ") " if self.preferred_first_name != "" else " ",
            self.last_name
        )

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





