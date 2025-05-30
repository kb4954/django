from django.db import models

class Student(models.Model):
    # 번호가 순차적으로 자동 증가
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    # 숫자타입
    grade = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=10,blank=True)
    hobby = models.CharField(max_length=100,blank=True)
    sdate = models.DateTimeField(auto_now=True) # sql-sysdate와 동일한 자동으로 들어가는 날짜
    memo = models.TextField(blank=True) # 빈공백을 넣어도 괜찮다는 뜻 
    
    
    # 관리자페이지뿐만아니라 다른곳에서도 보여줌 : 객체를 보기위해 str함수 사용
    def __str__(self):
        return f"{self.no},{self.name},{self.sdate}"