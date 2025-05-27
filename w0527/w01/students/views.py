from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from students.models import Student
from django.urls import reverse
# def list(request):
#     return HttpResponse("페이지연결")
# 학생정보리스트
def list(request):
    # Student 테이블 데이터 가져오기
    qs = Student.objects.all()
    context = {'list':qs}    # 딕셔너리타입으로 넘겨줌
    return render(request,'students/list.html',context)

# 학생등록페이지
def write(request):
    return render(request,'students/write.html')

# 학생등록저장
def write2(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    #request.POST[], request.POST.get()
    print("데이터 정보: ",name,major,grade,age,gender)
    qs = Student(name=name,major=major, grade=grade, age=age, gender=gender)
    qs.save()
    
    return redirect('students:list') 
    # students라는 app_name을 찾아서 list로 가라는 뜻 혹은 url링크로도 가능 '/students/list'
s    # return HttpResponseRedirect(reverse('students:list')
    # return render(request,'students/write.html')
    



# def list(request):
#     txt = '''
#         <html>
#             <head>
#             </head>
#         </html>
#         '''
        
#     return render(request,'list.html')