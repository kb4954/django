from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student

## 1. 학생전체보기
def list(request):
    qs= Student.objects.order_by('-id')
    context = {"list":qs, 'count':100, "id":'aaa'}
    return render(request,'students/list.html',context)

## 2. 학생입력하기
def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("request method : ", request.method)
        Student(name=name,major=major,grade=grade,age=age,gender=gender).save()
        print("Student 객체 저장")
        return redirect('/students/list')
    else: 
        return render(request,'students/write.html')
    
    
## 3. 학생상세보기
def view(request):
    name = request.GET.get('name')
    print("전달이름: ",name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'students/view.html',context)
    
    
    
    