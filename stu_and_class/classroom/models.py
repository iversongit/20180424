from django.db import models

# Create your models here.
class Classroom(models.Model):
    class_id = models.IntegerField()
    class_name = models.CharField(max_length=20)
    class_des = models.CharField(max_length=50)
    class Meta:
        db_table = 'classroom'