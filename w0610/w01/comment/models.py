from django.db import models
from board.models import Board
from member.models import Member # 작성자

class Comment(models.Model):
    cno = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board,on_delete=models.CASCADE) # 댓글을 달려면 원래 작성글이 필요함 작성글 = board ,게시글 삭제시
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING) # 작성자 탈퇴시 null처리
    cpw = models.CharField(max_length=20,null=True,blank=True)
    ccontent = models.TextField(blank=True)
    cdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.cno},{self.ccontent}"
    
    
    