from django.db import models

from users.models import Admin


class FeedbackItems(models.Model):
    feedback_items_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)

    def __str__(self):
        return str(self.title)


RATING_CHOICES = (
    ("*", "1"),
    ("**", "2"),
    ("***", "3"),
    ("****", "4"),
    ("*****", "5"),
)


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_items = models.ForeignKey(FeedbackItems, on_delete=models.CASCADE)
    rating = models.CharField(max_length=5, choices=RATING_CHOICES, default='*')
    message = models.TextField()
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback_id)
