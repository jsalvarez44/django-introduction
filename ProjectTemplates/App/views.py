import re
from django.shortcuts import render
from .models import Details

def index(request):
    if request.method == 'POST':
        type = request.POST['type']
        name = request.POST['name']
        
        obj = Details()
        obj.type = type
        obj.name = name
        obj.save()
        
    return render(request, 'index.html')
