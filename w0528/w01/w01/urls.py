from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/',include('students.urls')), # 학생정보리스트
    path('',include('home.urls')),#home
]
