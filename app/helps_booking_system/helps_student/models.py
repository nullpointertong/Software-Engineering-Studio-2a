from django.db import models
from django.utils.translation import ungettext_lazy as _
from django.contrib.auth.models import User

class session():
    session_ID = models.IntegerField(max_length=30,primary_key=True)
    # student_id = models.ForeignKey(studentAccount, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(staffAccount, on_delete=models.CASCADE)
    Location  = models.CharField(max_length=30)
    Session_time = models.IntegerField(max_length=30)
    Has_Finished  = models.BooleanField(max_length=30)
    No_Show = models.BooleanField(max_length=30)

class staffAccount():
    staff_id = models.IntegerField(max_length=30,primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # staff_id = models.ForeignKey()
    Email  = models.CharField(max_length=30)
    # Session histories (Array of <Session>)
    # No-show history
    # Sessions taught? 
    # Position
    # students? 
    Faculty =  models.CharField(max_length=30)
    Course =  models.CharField(max_length=30)
    Preferred_First_Name = models.CharField(max_length=30)
    Phone = models.IntegerField(max_length=30)
    Mobile = models.IntegerField(max_length=30)
    Best_contact_no = models.IntegerField(max_length=30)
    DOB = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Degree = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    First_language = models.CharField(max_length=30)
    Country_of_origin = models.CharField(max_length=30)
    Educational_Background = models.CharField(max_length=30)

class studentAccount():
    student_id = models.IntegerField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # staff_id = models.ForeignKey(staffAccount, on_delete=models.CASCADE)
    Email  = models.CharField(max_length=30)
    # Session histories (Array of <Session>)
    # No-show history
    Faculty =  models.CharField(max_length=30)
    Course =  models.CharField(max_length=30)
    Preferred_First_Name = models.CharField(max_length=30)
    Phone = models.IntegerField(max_length=30)
    Mobile = models.IntegerField(max_length=30)
    Best_contact_no = models.IntegerField(max_length=30)
    DOB = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Degree = models.CharField(max_length=30)
    Status = models.CharField(max_length=30)
    First_language = models.CharField(max_length=30)
    Country_of_origin = models.CharField(max_length=30)
    Educational_Background = models.CharField(max_length=30)

class Workshop():
    workshop_id = models.IntegerField(max_length = 30, primary_key=True)
    workshop_topic = models.CharField(max_length = 30)
    workshop_startdate = models.DateField()
    workshop_enddate = models.DateField()
    workshop_days = models.CharField(max_length=3)
    workshop_starttime = models.IntegerField(max_length = 4)
    workshop_endtime = models.IntegerField(max_length= 4)
    workshop_sessions_no = models.IntegerField(max_length= 2)
    workshop_places_avail = models.IntegerField(max_length= 3)

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





