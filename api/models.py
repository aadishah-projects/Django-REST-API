from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.AutoField()
    student_name = models.CharField(max_length= 100)
    student_age = models.IntegerField()
    student_description  = models.TextField()
    published_date = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.student_name