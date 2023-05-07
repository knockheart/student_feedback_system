from metadata.models import University, College, Course, Branch, Semester
from users import admin

admin.site.register(University)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Branch)


class SemesterAdmin(admin.ModelAdmin):
    model = Semester
    list_display = ['semester_id', 'description', 'year']


admin.site.register(Semester, SemesterAdmin)
