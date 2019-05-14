from dal import autocomplete
from helps_admin.models import StudentAccount, StaffAccount


class StudentAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return StudentAccount.objects.none()

        qs = StudentAccount.objects.all()

        if self.q:
            query = self.q
            if query.isalpha():
                qs = qs.filter(first_name__icontains=query) | qs.filter(last_name__icontains=query)
            elif query.isnumeric():
                qs = qs.filter(student_id__startswith=query)

        return qs


class StaffAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return StaffAccount.objects.none()

        qs = StaffAccount.objects.all()

        if self.q:
            query = self.q
            if query.isalpha():
                qs = qs.filter(first_name__icontains=query) | qs.filter(last_name__icontains=query)
            elif query.isnumeric():
                qs = qs.filter(staff_id__startswith=query)

        return qs
