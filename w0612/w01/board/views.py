from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

# form게시판 - get,post
def list(request):
    # db 데이터 모두 가져오기
    qs= Board.objects.all().order_by('-ntchk','-bgroup','bstep')    
    context = {'list':qs} # html 전달하는 방법 이거랑 json 방법
    return render(request,'board/list.html',context)




