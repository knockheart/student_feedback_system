from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AuthenticationForm

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import Admin, Student, Professor


class MyAdminSite(AdminSite):
    """
    App-specific admin site implementation
    """

    login_form = AuthenticationForm

    site_header = 'Todomon'

    def has_permission(self, request):
        """
        Checks if the current user has access.
        """
        print(request.__dict__.keys())
        print(request.__dict__["path"], request.__dict__["environ"]["QUERY_STRING"])
        if str(request.__dict__["environ"]["QUERY_STRING"]).lower().strip().strip("/").startswith("feedback"):
            return request.user.is_active
        else:
            return request.user.is_active and request.user.is_staff


site = MyAdminSite(name='myadmin')

admin.site = site


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = Admin

    list_display = ("student_id", "email", "is_staff", "is_active",)
    list_filter = ("student_id", "email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff", "is_active",
                "branch_id", "college_id",
                "student_id", "student_name", "phone_number",
                "groups", "user_permissions",
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Admin, CustomUserAdmin)


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['student_id', 'student_name', 'branch_id', 'email', 'phone_number']
    # list_editable = [ 'student_name', 'email', 'phone_number']


admin.site.register(Student, StudentAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    model = Professor
    list_display = ['professor_id', 'professor_name', 'branch_id', 'email', 'phone_number']


admin.site.register(Professor, ProfessorAdmin)
