from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'КомфортСтрой'
    context = {
        'title': title
    }
    return render(request, 'products/index.html', context)
