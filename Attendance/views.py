from django.shortcuts import render, redirect
from .models import Attendance
# Create your views here.

def index(request):
    # Views goes in here
    return render(request, 'index.html')

def save_attendance(request):
    if request.method == 'POST':
        name = request.POST['name']
        Department = request.POST['Department']
        level = request.POST['level']
        contact = request.POST['contact']

        data = Attendance.objects.create(name=name, 
                                         department=Department, 
                                         level=level, 
                                         contact=contact)
        data.save()
    return redirect('/')


def view_attendance(request):
    attendance = Attendance.objects.all()
    data = {'Attendance': attendance}

    return render(request, 'view_attendance.html', data)