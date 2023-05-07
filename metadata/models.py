from django.db import models


class University(models.Model):
    university_id = models.CharField(max_length=100, primary_key=True)
    university_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.university_name


class College(models.Model):
    college_id = models.CharField(max_length=200, primary_key=True)
    college_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    university_id = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.college_name


class Course(models.Model):
    course_id = models.CharField(max_length=200, primary_key=True)
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name


class Branch(models.Model):
    branch_id = models.CharField(max_length=200, primary_key=True)
    branch_name = models.CharField(max_length=200, unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.branch_name


class Semester(models.Model):
    semester_id = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.year} : {self.semester_id} : {self.description}"
