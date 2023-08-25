from django.shortcuts import HttpResponse
from datetime import datetime
# Create your views here.

def test_view(request):
    if request.method == 'GET':
        return HttpResponse("This is my first project")
        
def hello_views(request):
    return HttpResponse("Hello it's my new project")

def time(request):
    date = datetime.now().strftime("%d-%m-%Y - %H:%M:%S")
    return HttpResponse (date)

def goodbye(request):
    return HttpResponse("Goodbye user!")
