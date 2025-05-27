from django.shortcuts import render


def list(request):
    # request -> id = aaa
    id = request.POST.get("id") # 변수를 한개만 받을 수 있음
    pw = request.POST.get('pw')
    gender = request.POST.get('gender')
    tel = request.POST.get('tel')
    hobbys = request.POST.getlist('hobby') # 변수가 복수개라서 리스트혹은 딕셔너리 형태로 받아야함.
    print("입력된 id값 :",id)
    print("입력된 pw값 :",pw)
    print("입력된 gender값 :",gender)
    print("입력된 tel값 :",tel)
    print("입력된 hobby값 :",hobbys)
    
    context = {"id":id,"pw":pw,"gender":gender,"tel":tel,"hobby":hobbys}
    return render(request,'students/list.html',context)



def view(request):
    # get 방식으로 넘어옴 
    name = request.GET.get('name')
    age = request.GET.get('age')
    print("이름 :",name)
    print("나이 :",age)
    context = {"name":name,"age":age}
    return render(request,'students/view.html',context)

def test(request):
    #post방식
    name = request.POST.get("name")
    kor = int(request.POST.get("kor"))
    eng = int(request.POST.get("eng"))
    total = kor+eng
    hobbys = request.POST.getlist("hobby")
    context ={"name":name,"kor":kor,"eng":eng,"hobby":hobbys, "total":total}
    return render(request,'students/test.html',context)

def write(request):
    return render(request,'students/write.html')

def send(request,name,age):
    print("전달받은 값 : ",name,age)
    context = {"name":name,"age":age}
    return render(request,'students/send.html',context)