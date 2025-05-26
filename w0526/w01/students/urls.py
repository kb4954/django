from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    # views.py로 연결
    path('list/', views.list, name='list'), # 앱이름으로 연결할때 사용
    path('write/', views.write, name='write'), # 앱이름으로 연결할때 사용
    path('update/', views.update, name='update'), # 앱이름으로 연결할때 사용
    path('delete/', views.delete, name='delete'), # 앱이름으로 연결할때 사용
]
