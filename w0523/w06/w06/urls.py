from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('students/', include('students.urls')),
    path('', include('home.urls')),
]
