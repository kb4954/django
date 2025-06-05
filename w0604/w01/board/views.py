from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import F,Q 
# F : 검색된것에서 특정한 열을 가져올 수 있음 
# Q : end or not 등 연산자를 사용할때
from django.core.paginator import Paginator # 페이지를 분기하는 명령어


# 게시판 리스트 - 일반게시판 리스트, 검색게시판리스트
def list(request):
    # ㅎ현재 페이지 int 병경
    page = int(request.GET.get('page', 1)) # 없을 때 1페이지로 넘겨줌
    # serach
    search = request.GET.get('search','')
    category = request.GET.get('category','')
    print("검색데이터 : ", category, search)
    if search == '':
        # 게시글 전체 가져오기
        qs = Board.objects.order_by('-bgroup', 'bstep')
        # 페이지 분기
        paginator = Paginator(qs, 20)
        list = paginator.get_page(page)
        context = {"list":list, 'page':page}
        return render(request, 'board/list.html', context)
    else: # 검색으로 넘어온 경우
        # 게시글 전체 가져오기
        if category == 'all':
            qs = Board.objects.filter(
                Q(btitle__contains=search) | Q(bcontent__contains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        else:
            qs = Board.objects.filter(bcontent__contains=search)
        # 페이지 분기
        paginator = Paginator(qs, 20)
        list = paginator.get_page(page)
        context = {"list":list, 'page':page, 'search':search, 'category':category}
        return render(request, 'board/list.html', context)



# 게시글 보기
def view(request,bno):
    # 1. 1차 qs 값을 수정하는 방법
    # qs.bhit += 1
    # qs.save()
    # 2. F함수 사용 : 필터로 가져와야 적용됨.
    category= request.GET.get('category','')
    search= request.GET.get('search','')
    
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit =F('bhit')+1) # save까지 됨.
    
    context = {'board':qs[0],'category':category,'search':search }
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
        # bfile = request.POST.get('bfile')
        bfile = request.FILES.get('bfile','')
        print("파일부분 : ",request.FILES)
        print("write가져온 데이터 : ",bfile)
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
        bfile_pre = request.POST.get('bfile_pre','')
        bfile = request.FILES.get('bfile','')
        if not bfile:
            bfile = bfile_pre
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
        bfile = request.FILES.get('bfile')
        
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