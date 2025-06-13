from django.shortcuts import render
from board.models import Board
from comment.models import Comment



## 게시판 뷰페이지
def view(request,bno):
    ## db가져오기
    qs = Board.objects.get(bno=bno) # 만약 filter로 하게되면 1개도 리스트타입으로 넘어옴 
    c_qs = Comment.objects.filter(board=qs).order_by('-cno') # 역순정렬 # Comment에는 bno가 없음 그래서 board를 가져옴.
    context ={'board':qs, 'clist':c_qs} 
    return render(request,'board/view.html',context)

## 게시판 리스트
def list(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context ={'list':qs} # list.html로 받은 데이터를 qs로 가져오겠다
    return render(request,'board/list.html',context)