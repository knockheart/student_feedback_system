from django.contrib import admin as main_admin

from feedback_to_professors.models import FeedbackToProfessors
from users import admin


class FeedbackToProfessorsAdmin(main_admin.ModelAdmin):
    model = FeedbackToProfessors
    list_display = ['feedback_id', 'professor', 'user', 'rating', 'message', ]


admin.site.register(FeedbackToProfessors, FeedbackToProfessorsAdmin)
