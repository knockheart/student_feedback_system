from django.contrib import admin

from feedback.models import FeedbackItems, Feedback


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ['feedback_id', 'feedback_items', 'message', "user"]
    # list_filter = ["feedback_id"]


admin.site.register(FeedbackItems)
admin.site.register(Feedback, FeedbackAdmin)
