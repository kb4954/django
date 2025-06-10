from django.shortcuts import render
from board.models import Board

def list(request):
    qs = Board.objects.all(){bgrop}
    context = {'list':qs}
    return render(request,'board/list.html',context)