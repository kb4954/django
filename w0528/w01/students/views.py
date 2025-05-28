from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from students.models import Student # Student 테이블 불러오기

# 학생정보 삭제
def delete(request,name):
    print("삭제 이름: ",name)
    qs = Student.objects.get(name=name) # 해당되는 학생정보 검색
    qs.delete() # 삭제
    return redirect('/students/list')





# 학생정보 수정
def update(request,name):
    if request.method == 'GET':
        print("학생이름 : ",name)
        qs = Student.objects.get(name=name) # 해당되는 학생정보 검색
        context = {'stu':qs}
        return render(request,'students/update.html',context)
    else:
        name2 = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("입력된 정보 : ", name2, major, grade, age, gender)
        # DB수정
        # 1. 회원검색
        qs = Student.objects.get(name=name) # 해당되는 학생정보 검색
        # 2. 회원정보수정
        qs.name=name
        qs.major=major
        qs.grade=grade
        qs.age=age
        qs.gender=gender
        # 3. 저장
        qs.save()
        print("Student 객체 수정")
        return redirect('/students/list') # url

# 학생정보 상세보기
def view(request):
    name = request.GET.get('name')
    print("전달 이름 : ",name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보 리스트
def list(request):
    print(request)
    print(request.GET)
    print("request method : ", request.method)    
    # DB검색 
    # objects.all(): 전체가져오기, object.get(): 해당되는것 가져오기
    # objects.filter(): 검색가능
    qs = Student.objects.order_by("-id")
    # 딕셔너리 타입으로 전달 
    context = {"list":qs, 'count':100, 'id':'aaa'}
    return render(request,'students/list.html',context)


# 학생정보 등록
def write(request):
    if request.method == 'POST':  # post방식으로 들어올때 정보를 db에 저장
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print("request method : ", request.method)
        print("입력된 정보 : ", name, major, grade, age, gender)
        # DB저장 - save(),create()
        ## name, major, grade, age, gender
        ## Student 객체 테이블에 넣기 
        ## 데이터 저장하는 방법
        ## 1. qs = 데이터 , qs.save()
        ## 2. 데이터.save()
        ## 3. create()        
        Student(name=name, major=major, grade=grade, age=age, gender=gender).save()
        print("Student 객체 저장")
        return redirect('/students/list') # url
    
    else: # GET 방식으로 들어올때

        return render(request, 'students/write.html') # 파일찾기