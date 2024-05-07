from django.shortcuts import render

# Create your views here.

def home(request):
    print("I am Home Page")
    return render(request,'home.html')

def about(request):
    print("I am about Page")
    return render(request,'about.html')
def siteuc(request):
    print("I am about Page")
    return render(request,'siteuc.html')


