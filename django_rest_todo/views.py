from django.shortcuts import render

def index(request):
    return render(request, 'django_rest_todo/index.html')