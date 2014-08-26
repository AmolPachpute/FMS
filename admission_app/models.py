from django.db import models
from schools.models import Academic_Year , StudentGroup , Child

class StudentPersonalDetails(models.Model):
    academic = models.ForeignKey(Academic_Year)
    child = models.ForeignKey(Child)
    student_group = models.ForeignKey(StudentGroup)

class PreviousEducationDetails(models.Model):
    student = models.ForeignKey(StudentPersonalDetails)
    institution_name = models.CharField(max_length = 200)
    course = models.CharField(max_length = 200)
    pasing_year = models.CharField(max_length = 200)
    marks = models.CharField(max_length =200)
