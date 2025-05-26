from django.shortcuts import render
from students.models import Student

#출력하기위한 
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request,'list2.html',context) # 변수 전달

