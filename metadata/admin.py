from django.contrib import admin

from metadata.models import University, College, Course, Branch

admin.site.register(University)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Branch)
