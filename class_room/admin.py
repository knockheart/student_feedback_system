from class_room.models import Subject
from users import admin


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    # list_display = [field.name for field in Subject._meta.get_fields()]
    list_display =[
        'subject_id', 'subject_name', 'description', 'branch_id', 'semester_id', 'college_id', 'professor_id'
    ]

admin.site.register(Subject, SubjectAdmin)
