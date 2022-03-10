from django.shortcuts import render

def simpleRender(request):
    context = {
        'name': 'Sebastian',
        'lastname': 'Alvarez',
    }
    return render(request, 'index.html', context)
