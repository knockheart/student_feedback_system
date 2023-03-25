"""
WSGI config for student_feedback_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from metadata.models import Course, University
from users.models import Branch, College, Admin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_feedback_system.settings')

application = get_wsgi_application()

users = Admin.objects.all()
if not users:
    course = Course(course_name="BE")
    course.save()
    branch = Branch(branch_name="ECE", course_id=course)
    branch.save()

    university = University(university_name="VTU", address="NA")
    university.save()
    college = College(college_name="UBDTCE", address="NA", university_id=university)
    college.save()

    Admin.objects.create_superuser(
        # username="a@gmail.com",
        email="a@gmail.com",
        password="admin#123456",
        is_active=True,
        is_staff=True,
        branch_id=Branch.objects.get(branch_id=branch.branch_id),
        college_id=College.objects.get(college_id=college.college_id),
    )
