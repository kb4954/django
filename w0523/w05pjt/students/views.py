from django.shortcuts import render
from django.http import HttpResponse
# db접근하기위해 
from students.models import Student

# Create your views here.

## 학생리스트 전제
def list(request):
    ## 데이터 모두 가져오기
    qs = Student.objects.all()
    context = {'list':qs}
    print(qs)
    ## html 페이지 연결
    return render(request,'list.html',context)

## 학생 상세 페이지
def view(request):
    name ='유관순'
    qs = Student.objects.get(name=name)
    context ={'stu':qs}
    print(qs)
    return render(request,'view.html',context)


def write(request):
    return render(request,'write.html')

def delete(request):
    return render(request,'delete.html')