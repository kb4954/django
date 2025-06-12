from django.urls import path,include
from . import views

app_name='ajaxdata'
urlpatterns = [
    path('bwrite/', views.bwrite, name='bwrite'),

]
