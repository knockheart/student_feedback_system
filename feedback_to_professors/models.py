from django.db import models

from class_room.models import Subject
from metadata.models import Semester
from users.models import Professor, Student

RATING_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


class FeedbackToProfessors(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=None)
    rating = models.CharField(max_length=5, choices=RATING_CHOICES, default='*')
    message = models.TextField()

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.feedback_id)
