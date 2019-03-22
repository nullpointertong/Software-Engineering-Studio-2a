from django.db import models
from django.utils.translation import ungettext_lazy as _
from django.contrib.auth.models import User


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