from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, context={'title': 'evak24-7.ru'}, template_name='evak_main/index.html')
