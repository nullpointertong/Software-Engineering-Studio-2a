from django.db import models
from django.utils.translation import ungettext_lazy as _
from django.contrib.auth.models import User

class SessionListField(models.Field):
    '''Field for list of sessions.
    Accepts a list argument'''

    def __init__(self, sessions=[], *args, **kwargs):
        self.sessions = sessions
        self.max_length = 2048
        kwargs['max_length'] = self.max_length 
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Must return arguments to pass to __init__ for reconstruction
        if self.sessions != []:
            kwargs['sessions'] = self.sessions
        del kwargs['max_length']
        return name, path, args, kwargs

    def db_type(self, connection):
        return 'sessionlist', 'char({})'.format(self.max_length)

    def from_db_value(self, value, expression, connection):
        return value

    def to_python(self, value):
        pass
    


class session():
    session_ID = models.IntegerField(primary_key=True)
    student_id = models.ForeignKey(
        'studentAccount',
        on_delete=models.CASCADE
    )
    staff_id = models.ForeignKey(
        'staffAccount',
        on_delete=models.CASCADE
    )
    Location  = models.CharField(max_length=30)
    Session_time = models.DateTimeField()
    Has_Finished  = models.BooleanField()
    No_Show = models.BooleanField()

class staffAccount():
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

class studentAccount():
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





