from django.core.management.base import BaseCommand, CommandError
from helps_admin.models import StudentAccount, StaffAccount
from datetime import datetime
from random import randint
import uuid

def generate_DOB(min_age : int, max_age : int):
    """Generate a date of birth datetime given max and min year age"""
    year = randint(datetime.now().year - 69, datetime.now().year - 18)
    month = randint(1, 12)
    if month == 2: # if month is February
        # 29 days if leap year, 28 if not
        day = randint(1, 29) if year % 4 == 0 else randint(1, 28)
    else:
        # Account for 30 or 31 day months
        day = randint(1, 30) if month in [4, 6, 9, 11] else randint(1, 31)
    return datetime(year=year, month=month, day=day)

class Command(BaseCommand):
    help = "Populates the database with x number of StaffAccount and StudentAccount entries"
    NAME_COUNT = 10000 # Length of names.txt file

    def create_entries(self, count):
        START_ID = 10000000 # Using 8 digit numbers (user/staff ids)
        # Every initial id is user, every intial + 1 is staff:
        for user_id in range(START_ID, START_ID + (count * 2)):
            # Populate the database
            with open("names.txt","r") as f:
                for i, line in enumerate(f): # Iterate over file
                    if i == user_id - START_ID: # Match current new name with user_id
                        # even i = student, odd i = staff, i is index 0
                        if i % 2 == 0:
                            user = StudentAccount()
                            user.student_id = str(user_id)
                        else:
                            user = StaffAccount()
                            user.staff_id = str(user_id)
                        user.first_name, user.last_name = line.strip("\n").split(" ")
                        user.email = "{}.{}@email.com".format(user.first_name, user.last_name)
                        user.phone = "98{}".format(str(uuid.uuid4().int)[:6])
                        user.mobile = "04{}".format(str(uuid.uuid4().int)[:8])
                        user.best_contact_no = user.mobile
                        user.DOB = generate_DOB(18, 69)
                        # Save to database
                        user.save()

    def add_arguments(self, parser):
        parser.add_argument('entry_count', nargs=1, type=int)

    def handle(self, *args, **options):
        if options["entry_count"][0] > self.NAME_COUNT:
            raise CommandError("Entry count ({}) is larger than available entries ({}) in names.txt".format(options["entry_count"], self.NAME_COUNT))
        else:
            self.create_entries(options["entry_count"][0])
