from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F # 검색된것에서 특정한 열을 가져올 수 있음 

# 게시판 리스트
def list(request):
    # 게시글 전체 가져오기
    qs = Board.objects.order_by('-bgroup','bstep') # 같은게 있을때만 bstep으로 조정함
    context = {'list':qs}
    
    return render(request,'board/list.html',context)

# 게시글 보기
def view(request,bno):
    # 1. 1차 qs 값을 수정하는 방법
    # qs.bhit += 1
    # qs.save()
    # 2. F함수 사용 : 필터로 가져와야 적용됨.
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit =F('bhit')+1) # save까지 됨.
    
    context = {'board':qs[0]}
    return render(request,'board/view.html',context)

# 게시글 쓰기
def write(request):
    if request.method=='GET':
        return render(request,'board/write.html')
    elif request.method=='POST':
        # 데이터 가져오기
        id = request.POST.get('id') # 섹션에서 가져옴
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print("가져온 데이터 : ",id,btitle,bcontent,bfile)
        # 데이터 저장
        # 방법 1
        # Board(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile).save()
        # 방법 2 create
        qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bfile=bfile)
        qs.bgroup = qs.bno # 나중에 수정할때 group이 필요함.
        qs.save()
        context ={'msg':1}
        return render(request,'board/write.html',context)
    
    
def update(request,bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/update.html',context)
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        # qs.bfile = bfile
        qs.save()
        context = {'msg':1,'board':qs}
        return render(request,'board/update.html',context)
    
    
    
def delete(request,bno):
    ## 게시글 삭제
    Board.objects.get(bno=bno).delete()
    return redirect('/board/list/')


# 답글달기 - 답글달기 페이지 열기, 답글달기 저장
def reply(request,bno):
    if request.method=='GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request,'board/reply.html',context)
    elif request.method=='POST':
        id = request.POST.get('id') # 나중에 session_id 가져옴
        bgroup = request.POST.get('bgroup') # 부모의 bgroup
        bstep = int(request.POST.get('bstep')) # 부모의 bstep
        bindent = int(request.POST.get('bindent')) # 부모의 bindent
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        ## 답글달기 저장
        # 1. gt, lt, gte, lte
        # 모든 자식들은 전부 bstep을 1씩 증가시켜야함.
        # 부모보다 bstep 더 많은 것은 전부 bstep 1씩 증가 
        # F함수 현재 찾아진 컬럼의 값을 모두 가져옴.
        reply_qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
        reply_qs.update(bstep = F('bstep')+1)
        # 2. reply 1씩 증가후 , db저장
        qs = Board.objects.create(btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
        
        
        
        
        
        context = {'msg':1,'board':qs}
        return render(request,'board/reply.html',context)