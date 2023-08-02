from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Jock"
    # return HttpResponse("Welcome to django app")
    return render(request,'index.html',{'name':name})

def counter(request):
    input = request.POST['words']
    input = len(input)
    return render(request,'counter.html',{'input':input})