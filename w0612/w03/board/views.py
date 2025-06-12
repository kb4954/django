from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

# form게시판 - get,post
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
        context = {'list':qs}
        return render(request,'board/list.html',context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print('넘어온데이터: ',id,btitle,bcontent)
        # db저장
        qs = Board.objects.create(id=id,btitle=btitle)
        qs.bgroup=qs.bno
        qs.save()
    
    
        return redirect('/board/list/')

def view(request):
    bno = request.GET.get('bno')
    print('넘어온 bno : ',bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request,'board/view.html',context)

# 2. form - get,post
def list2(request):
    if request.method=='GET':
        qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep') # 답글달기 기능이 없으면 이 정렬도 필요없음
        context = {'list':qs}
        return render(request,'board/list2.html',context)
    elif request.method=='POST':
        return render(request,'board/list2.html')
           
def view2(request,bno):
    print("넘어온 데이터 :", bno)
    qs = Board.objects.get(bno=bno)
    context ={'board':qs}
    return render(request,'board/view2.html',context)

#------------------------------------------------------------------------


def list3(request):
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    context = {'list':qs}
    return render(request,'board/list3.html',context)

# ajax3 - Board의 모든데이터 가져오기
def ajax3(request):
    qs =Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print(qs)
    a = request.POST.get('sampleId')
    print("넘어온데이터 :",a)
    list_qs = serializers.serialize('json',[qs])
    print("변경타입 : ",list_qs)
    context={'result':'성공','list':list_qs} # 타입이 쿼리셋이서 못가지고옴 
    return JsonResponse(context)


