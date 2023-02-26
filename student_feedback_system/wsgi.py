"""
WSGI config for student_feedback_system project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from users.models import Branch, College, CustomUser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_feedback_system.settings')

application = get_wsgi_application()

users = CustomUser.objects.all()
if not users:
    CustomUser.objects.create_superuser(
        # username="a@gmail.com",
        email="a@gmail.com",
        password="admin#123456",
        is_active=True,
        is_staff=True,
        branch_id=Branch.objects.get(branch_id="1"),
        college_id=College.objects.get(college_id="1"),
    )
