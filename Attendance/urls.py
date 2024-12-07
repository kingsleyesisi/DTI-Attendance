from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('save_attendance', views.save_attendance, name='save_attendace'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
]