from django.urls import path,include
from . import views

app_name='students'
urlpatterns = [
    path('list/', views.list,name='list'),
    path('write/', views.write,name='write'),
    path('writeOk/', views.writeOk,name='writeOk'),
    # html -> server 1. 파라미터 2. api 방식 3. 자바스크립트방식
    # 2번째 방식 사용 <str:name>
    path('view/<int:no>/', views.view,name='view'),
    path('update/<int:no>/', views.update,name='update'), # 수정페이지 열기
    path('updateOk/', views.updateOk,name='updateOk'), # 수정완료
    path('delete/<int:no>/', views.delete,name='delete'), # 학생정보삭제
]