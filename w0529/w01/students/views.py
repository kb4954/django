from django.shortcuts import render,redirect
from students.models import Student


# 학생정보리스트
def list(request):
    # render 폴더앞에 / 안붙임
    # Students table 연결
    qs = Student.objects.all()
    context = {'list':qs}    
    
    return render(request,'students/list.html',context)

# 학생정보등록페이지열기
def write(request):
    # if request.method =='GET':
        return render(request,'students/write.html')
    # else: # /if request.method =='POST':
    #     return redirect('/students/list/')
           
# 학생정보 저장 
def writeOk(request):
    name = request.POST.get('name') # == request.POST['name'] 
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobbys = request.POST.getlist('hobby')
    # 리스트타입 -> str타입으로 변경해줘야함.
    hobbys = ','.join(hobbys)
    print("저장정보 hobby: ",hobbys) 
    Student(name=name,major=major,grade=grade,age=age,gender=gender,memo='등록합니다.',hobby=hobbys).save()
      
    
    return redirect('/students/list/')

## 상세보기
def view(request,no): # urls에서 no를 받았으므로
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None
    print('전달번호 : ',no)
    context = {'stu':qs}
    return render(request,'students/view.html',context)

# 학생정보수정페이지 열기
def update(request,no):
    qs = Student.objects.get(no=no) # set타입 1개
    context ={'stu':qs}
    # qs = Student.objects.filter(no=no) # 데이터 타입 - 리스트타입 
    # context ={'stu':qs[0]} # filter는 리스트타입으로 넘어오므로 꼭 숫자를 적어줘야함 못찾아도 에러가 나지 않음 
    return render(request,'students/update.html',context)

# 학생정보수정완료
def updateOk(request):
    no = request.POST.get('no')
    # 데이터 검색
    qs = Student.objects.get(no=no)
    # 데이터 수정
    qs.name=request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby=','.join(hobby)
    qs.hobby=hobby
    qs.save()
    return redirect(f'/students/view/{no}')

def delete(request,no):
    Student.objects.get(no=no).delete()
    return redirect('/students/list/') # 삭제해서 view로 보낼 수 없음
    # return redirect('/students:list/') # 삭제해서 이름으로도 보낼 수 있음 앱이름-리스트(path name)
    # 나중에는 url보다는 name방식으로 하는게 더 좋음
    