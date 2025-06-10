from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers # json 타입으로 생성해줌 
from django.views.decorators.csrf import csrf_exempt


def list(request):
    return HttpResponse('데이터전달')
