from django.shortcuts import render
from django.http import HttpResponse

# db 접근
from students.models import Student

# Create your views here.
## 학생 리스트 전체
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list.html',context)

def view(request):
    name='유관순'
    qs = Student.objects.get(name=name)
    context ={'stu':qs}
    return render(request,'view.html',context)


