from django.shortcuts import render
from django.http import JsonResponse

def list(request):
    return render(request,'board/list.html')

# form 으로 보내는 방법
def view(request):
    id= request.POST.get('id')
    name= request.POST.get('name')
    context = {'id':id,'name':name}
    return render(request,'board/view.html',context)

# ajax 으로 보내는방법
def view2(request):
    id= request.POST.get('id','')
    name= request.POST.get('name','')
    # QuerySet, QueryList -> list 타입
    # models db데이터가 있으면 list타입으로 변경 후 전송해야함.
    
    
    
    context = {'id':id,'name':name,'result':'success','pw':'1111'}
    
    return JsonResponse(context)
        
         
    
    