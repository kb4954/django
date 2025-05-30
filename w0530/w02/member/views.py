from django.shortcuts import render
from member.models import Member
def login(request):
    if request.method=='GET':
        return render(request,'member/login.html')
    elif request.method =='POST':
        id = request.POST.get('id')    
        pw = request.POST.get('pw')
        print("아이디, 패스워드 :",id,pw)
        try:
            qs = Member.objects.get(id=id)
            if qs.pw ==pw:
                request.session['session_id'] = id
                txt = 1
            else: txt = -1
        except: txt=0
        
        context={'msg':txt}
        return render(request,'member/login.html',context)
        
        
        
    return render(request,'member/login.html')
        
    
    
