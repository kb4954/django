from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/',views.list,name='list'),
    path('write/',views.write,name='write'), # wrtie.html - GET,POST
    path('view/',views.view,name='view'), # view.html
    path('update/<str:name>/',views.update,name='update'), # update.html
    path('delete/<str:name>/',views.delete,name='delete'), # delete.html
]
