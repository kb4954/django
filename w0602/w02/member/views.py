from django.shortcuts import render

def login(request):
    if request.method == 'GET':
        print("모든 쿠키 : ",request.COOKIES)
        return render(request,'member/login.html')
        
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        print("아이디,패스워드 : ",id,pw)
    
        return render(request,'member/login.html')
    
    
    
