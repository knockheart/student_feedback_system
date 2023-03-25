from django.contrib import admin as student_admin
from django.contrib.admin import AdminSite

from users.models import Student, Professor


class StudentAdminSite(AdminSite):
    site_header = "Student Feedback Portal"
    site_title = "Student Feedback Portal"
    index_title = "Welcome to Student Feedback Portal"


student_admin_site = StudentAdminSite(name='student_portal')


class StudentAdmin(student_admin.ModelAdmin):
    model = Student
    list_display = ['student_id', 'student_name', 'branch_id', 'email', 'phone_number']
    # list_editable = [ 'student_name', 'email', 'phone_number']

    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.filter(email=request.user)


student_admin_site.register(Student, StudentAdmin)


class ProfessorAdmin(student_admin.ModelAdmin):
    model = Professor
    list_display = ['professor_id', 'professor_name', 'branch_id', 'email', 'phone_number']


student_admin_site.register(Professor, ProfessorAdmin)
