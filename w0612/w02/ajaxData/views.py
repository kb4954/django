from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

def write(request):
    context={}
    return JsonResponse(context)


def blist(request):
    ## ajax에서 전송된 데이터 받기
    # id = request.POST.get('id') # 초반에 DB를 작성하지 않았을때 연결확인을 위해 context으로 보내서 확인하기
    # context ={'result':'success'}

    ## db연결해서 board에 있는 모든데이터를 가져오기 
    qs = Board.objects.all().order_by('-ntchk','-bgroup','bstep') # 여러개 넘어오기때문에 QuerySet list 타입임
    
    ## json으로 타입변경 
    l_qs =list(qs.values())

    ## ajax 데이터 전송시킴    
    context = {'result':'success','list':l_qs}
    return JsonResponse(context)
