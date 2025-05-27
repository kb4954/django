from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')), # students app > urls.py
    path('event/', include('event.urls')),
    path('stuscore/', include('event.urls')),
    path('', include('home.urls')),
]
