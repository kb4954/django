from django.db import models

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)   # 작성자
    btitle = models.CharField(max_length=1000) # 제목
    bcontent = models.TextField() # 내용
    
    # 답글달기에 필요한 것들
    bgroup = models.IntegerField(default=0) # 답글달기로 되어있는것들을 하나로 묶어줌
    bstep = models.IntegerField(default=0) # 답글달기 순서
    bindent = models.IntegerField(default=0) # 들여쓰기
    #-----------------------------------------
    bhit = models.IntegerField(default=0)
    bfile = models.CharField(max_length=100,null=True,blank=True)
    bdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.bno},{self.btitle},{self.bgroup}"
    