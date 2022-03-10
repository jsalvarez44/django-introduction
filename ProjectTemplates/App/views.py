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

def readData(request):
    data = request.POST.get('id')
    
    try:
        data_send = data
        SQLExtractor = Details.objects.get(id=data_send)
        data = (SQLExtractor.name, SQLExtractor.type)
    except:
        data = data
        
    print(data)
    return render(request, 'readData.html', {'data': data})
