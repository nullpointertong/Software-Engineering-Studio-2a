from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from random import randint
from functools import wraps
from datetime import date, time

from helps_student.models import Workshop, StaffAccount, StudentAccount

def retry_query(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ObjectDoesNotExist:
                print("Error: object does not exist. Please retry.")
    return wrapper

def safe_to_int(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except (TypeError, ValueError):
                print("Error: Expected an int but did not get one. Please retry")
    return wrapper

@retry_query
def get_staff():
    _id = input("Input Staff ID: ")
    staff = StaffAccount.objects.get(staff_id=_id)
    print("Retrieved staff:\n" + str(staff))
    return staff

@retry_query
def get_student():
    _id = input("Input Student ID: ")
    student = StudentAccount.objects.get(student_id=_id)
    print("Retrieved student:\n" + str(student))
    return student

@safe_to_int
def get_student_list():
    num = int(input("Number of students to add: "))
    student_list = []
    while num > 0:
        student_list.append(get_student())
        num -= 1
    return student_list

@safe_to_int
def get_date(when: str):
    print("Setting up {} date".format(when))
    y = int(input("\t {} year: ".format(when)))
    m = int(input("\t {} month: ".format(when)))
    d = int(input("\t {} day: ".format(when)))
    return date(year=y, month=m, day=d)

@safe_to_int
def get_time(when: str):
    print("Setting up {} time".format(when))
    h = int(input("\t {} hour: ".format(when)))
    m = int(input("\t {} minute: ".format(when)))
    s = int(input("\t {} second: ".format(when)))
    return time(hour=h, minute=m, second=s)

@safe_to_int
def get_num_sessions():
    return int(input("Number of sessions: "))

class Command(BaseCommand):
    help = "Generates a new Workshop entry."

    # def add_arguments(self, parser):
    #     parser.add_arguments(
    #         "--auto",
    #         action="store_true",
    #         help="Automatically randomly assign existing staff and students."
    #     )

    def handle(self, *args, **options):
        workshop = Workshop(
            workshop_ID = str(int(Workshop.objects.all().order_by("-workshop_ID")[0].workshop_ID) + 1),
            staff = get_staff(),
            max_students = input("Max number of students: "),
            skill_set_name = input("Skill set name: "),
            start_date = get_date("start"),
            end_date = get_date("end"),
            start_time = get_time("start"),
            end_time = get_time("end"),
            days = input("Number of days: "),
            room = input("Room: ")
        )
        workshop.no_of_sessions = get_num_sessions()
        workshop.save() # Must save before adding students
        workshop.students.set(get_student_list())
        self.stdout.write(self.style.SUCCESS("Successfully added workshop"))

