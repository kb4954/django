from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers # json 타입으로 생성해줌 
from django.views.decorators.csrf import csrf_exempt # csrf토큰이 없을때 예외처리를 해줌
from member.models import Member
from board.models import Board
from comment.models import Comment


def cdelete(request):
    # cno 데이터 확인
    cno = request.POST.get('cno')
    print('하단댓글번호: ',cno)
    qs = Comment.objects.delete(cno=cno)
    qs.delete()
    context = {'result':'success'}
    return JsonResponse(context)



# 하단댓글 저장
def cwrite(request):
    # id = request.session['session_id'] # 로그인이 되어 있어야 하단 댓글 가능 
    id = 'aaa'
    member = Member.objects.get(id=id)
    bno = request.POST.get('bno',1)
    board = Board.objects.get(bno=bno)
    cpw = request.POST.get('cpw','')
    ccontent = request.POST.get('ccontent','')
    print('넘어온 데이터 :',cpw,ccontent)
    # QuerySet 타입 -> list 타입 
    qs = Comment.objects.create(board=board,member=member,cpw=cpw,
                                ccontent=ccontent)
    
    # filter 리스트타입으로 리턴
    list_qs = list(Comment.objects.filter(cno=qs.cno).values())
    print('list_qs: ',list_qs)
    context = {'result':'success','comment':list_qs}
    
    return JsonResponse(context)
