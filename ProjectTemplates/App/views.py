from django.shortcuts import render

def simpleRender(request):
    data = request.POST.get('name')
    try:
        data_clone = data
        
        if data_clone == 'Hello':
            data = 'Hi, how are you?'
    except:
        data = data
    
    return render(request, 'index.html', {'data': data})
