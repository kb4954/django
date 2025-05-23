from django.urls import path,include
from . import views # 모든파일을 찾아 views찾는 명령어

app_name = 'students'
urlpatterns = [
    path('list/',views.list,name='list'),   # 학생전체리스트

]
