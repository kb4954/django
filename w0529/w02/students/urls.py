from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'),
    path('writeOk/',views.writeOk,name='writeOk'),
]
