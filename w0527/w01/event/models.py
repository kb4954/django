from django.db import models
from datetime import datetime
# Event 테이블 생성해서

class Event(models.Model):
    no = models.AutoField(primary_key=True) # 자동번호부여
    title = models.CharField(max_length=1000)
    startdate = models.DateField()
    enddate = models.DateField()
    rdate = models.DateTimeField(default=datetime.now(),blank=True) # 빈공백으로 넣을 수 있지만 default로 시간을 넣어달라
    
    
    def __str__(self):
        return f"{self.no},{self.title}"