from django.db import models

# Create your models here.



## ORM(Object-Relational Mapping)
## class 객체 등록하면 db가 자동으로 생성 = ORM

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0) 
    grade = models.IntegerField(default=0) 
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name+","+self.major
