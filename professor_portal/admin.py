from django.contrib import admin as student_admin
from django.contrib.admin import AdminSite

from users.models import Student, Professor


class ProfessorAdminSite(AdminSite):
    site_header = "Professor Portal"
    site_title = "Professor Portal"
    index_title = "Welcome to Professor Portal"


professor_admin_site = ProfessorAdminSite(name='professor_portal')


class ProfessorAdmin(student_admin.ModelAdmin):
    model = Professor
    list_display = ['student_id', 'student_name', 'branch_id', 'email', 'phone_number']

    # list_editable = [ 'student_name', 'email', 'phone_number']

    def get_queryset(self, request):
        qs = super(ProfessorAdmin, self).get_queryset(request)
        # if request.user.is_superuser:
        #     return qs
        return qs.filter(email=request.user)


professor_admin_site.register(Student, ProfessorAdmin)


class ProfessorAdmin(student_admin.ModelAdmin):
    model = Professor
    list_display = ['professor_id', 'professor_name', 'branch_id', 'email', 'phone_number']


professor_admin_site.register(Professor, ProfessorAdmin)
