from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board


# Create your views here.
# ajaxWrite 글쓰기 ajax 1. 데이터전송유무 2.  db저장 
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print("html에서 server측으로 전달한 데이터 : ",id,btitle,bcontent)
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup=qs.bno
    qs.save()
    # JSON데이터로 변환 : serializers or list타입으로 변환
    # list()으로 변환 
    # l_qs = list(Board.objects.filter(bno=qs.bno).values())
    list(Board.objects.filter(bno=qs.bno).values())
    context = {'result':'success'}
    return JsonResponse(context)