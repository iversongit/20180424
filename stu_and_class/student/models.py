from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    sex = models.BooleanField()
    classno = models.IntegerField()
    class Meta:
        db_table = 'student'