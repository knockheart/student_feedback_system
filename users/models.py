from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from metadata.models import Branch, College
from .managers import CustomUserManager


# class University(models.Model):
#     university_id = models.CharField(max_length=100, primary_key=True)
#     university_name = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.university_name
#
#
# class College(models.Model):
#     college_id = models.CharField(max_length=200, primary_key=True)
#     college_name = models.CharField(max_length=200)
#     address = models.CharField(max_length=200)
#
#     university_id = models.ForeignKey(University, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.college_name
#
#
# class Course(models.Model):
#     course_id = models.CharField(max_length=200, primary_key=True)
#     course_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.course_name
#
#
# class Branch(models.Model):
#     branch_id = models.CharField(max_length=200, primary_key=True)
#     branch_name = models.CharField(max_length=200, unique=True)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.branch_name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    student_id = models.CharField(max_length=200)
    student_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ['is_staff']
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # this methods are require to login super user from admin panel
    def has_perm(self, perm, obj=None):
        return self.is_staff

    # this methods are require to login super user from admin panel
    def has_module_perms(self, app_label):
        return self.is_staff
