from django.shortcuts import render
from django.http import JsonResponse
from comment.models import Comment
from member.models import Member
from board.models import Board

## 하단댓글 수정
def cupdate(request):
    cno = request.POST.get('cno')
    ccontent = request.POST.get('ccontent')
    print('넘어온 cno: ',cno,ccontent)
    ## db 수정저장
    qs = Comment.objects.get(cno=cno)
    qs.ccontent = ccontent
    qs.save()
    # json 타입으로 변경
    json_qs = list(Comment.objects.get(cno=cno).values())
    context = {'result':'success','comment':json_qs}
    return JsonResponse(context)


## 하단댓글 등록 삭제
def cdelete(request):
    cno = request.POST.get('cno')
    print('넘어온 cno: ',cno)
    ## db 삭제
    Comment.objects.get(cno=cno).delete()
    context ={'result':'success'}
    return JsonResponse(context)



## 하단댓글 등록 -> json 타입리턴
def cwrite(request):
    # html에서 디장고로 데이터 전달
    id = request.POST.get('id')
    bno = request.POST.get('bno')
    cpw = request.POST.get('cpw')
    ccontent = request.POST.get('ccontent')
    print('넘어온데이터: ',bno,id,cpw,ccontent)
    # id-> member로 변경
    # bno-> board로 변경해야됨.
    member = Member.objects.get(id=id)
    board = Board.objects.get(bno=bno)
    
    ## db 저장
    qs = Comment.objects.create(member=member,board=board,cpw=cpw,ccontent=ccontent)
    print(qs) # QuerySet타입
    
    ## Json 타입 변경 - QuerySet list 타입은 list 타입으로 바로 변경
    json_qs  = list(Comment.objects.filter(cno=qs.cno).values())
    print(json_qs)
    context = {'result':'success','comment':json_qs}
    
    return JsonResponse(context)

## 하단댓글 리스트 -> json 타입리턴
def clist(request):
    context = {'result':'success'}
    return JsonResponse(context)