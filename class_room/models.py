from django.db import models

from metadata.models import Branch, Semester, College
from users.models import Professor


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject_name}"

    @staticmethod
    def __get_all_attributes__():
        return Subject.__dict__

#
# class Class(models.Model):
#     semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE)
#     professor_id = models.ForeignKey(Professor, on_delete=models.CASCADE)
#     year = models.IntegerField()
#
#     def __str__(self):
#         return f"{self.year} : {self.semester_id} : {self.description}"
