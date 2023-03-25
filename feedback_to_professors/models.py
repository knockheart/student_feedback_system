from django.db import models

from users.models import Admin, Professor

RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class FeedbackToProfessors(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=5, choices=RATING_CHOICES, default='*')
    message = models.TextField()

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback_id)
