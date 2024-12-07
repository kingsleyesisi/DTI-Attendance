from django.shortcuts import render

# Create your views here.

def index(request):
    # Views goes in here
    return render(request, 'index.html')

def save_attendance(request):
    if request.method == 'POST':
        username = request.get('name')
        department = request.get('Department')
        level = request.get('level')
        