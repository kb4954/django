from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def list(request):
    return render(request,'list.html')
    # return HttpResponse('리스트 페이지연결')
    
    ## templates 폴더에 list.html 파일 존재


def view(request):
    return render(request,'view.html')


def write(request):
    return render(request,'write.html')

def delete(request):
    return render(request,'delete.html')