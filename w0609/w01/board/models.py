from django.db import models
from member.models import Member
class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100, null=True)   # 작성자
    # 외래키 (Foreign Key)
    member = models.ForeignKey(Member,on_delete=models.SET_NULL, null=True) # DO_NOTHING: 어떤것도 관여하지않는다.
    # member = models.ForeignKey(Member,on_delete=models.CASCADE) # CASCADE: 회원탈퇴시 모두 삭제 , SET_NULL, null=True : 회원탈퇴시 널값을 집어넣음
    btitle = models.CharField(max_length=1000) # 제목
    bcontent = models.TextField() # 내용
    # TextField: 글자수 제한이 없는 데이터
    
    # 답글달기에 필요한 것들
    bgroup = models.IntegerField(default=0) # 답글달기로 되어있는것들을 하나로 묶어줌
    bstep = models.IntegerField(default=0) # 답글달기 순서
    bindent = models.IntegerField(default=0) # 들여쓰기
    #-----------------------------------------
    bhit = models.IntegerField(default=0) # 조회수
    bfile = models.ImageField(null=True,blank=True,upload_to='board')
    # IntegerField : 모든파일 업로드 가능
    ntchk = models.IntegerField(default=0)
    # bfile = models.FileField(null=True,blank=True,upload_to='board')
    # FileField: 모든파일 업로드가능 
    bdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.bno},{self.btitle},{self.bgroup}"
    