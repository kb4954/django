from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

# 게시글 삭제
def bdelete(request):
    bno = request.POST.get('bno')
    # db삭제
    qs = Board.objects.get(bno=bno).delete()
    context = {'result':'success'}
    return JsonResponse(context)

def bwrite(request):
    id= request.POST.get('id')
    btitle= request.POST.get('btitle')
    bcontent= request.POST.get('bcontent')
    # db 저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    
    
    
    context = {'result':'success','board':l_qs}
    return JsonResponse(context)


# ajaxWrite 글쓰기 ajax 1. 데이터전송유무 2.  db저장 
def blist(request):
    ## db 게시글 전체 가져오기
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep')
    print('queryset 타입 : ',qs)
    ## json타입으로 변경
    l_qs = list(qs.values())
    print('리스트타입 : ',l_qs)
    context = {'result':'success','list':l_qs}
    return JsonResponse(context)
