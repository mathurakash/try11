from django.shortcuts import render

# Create your views here.

def home(request):
    print("Home Page")
    return render(request,"app1/home.html")

def about(request):
    print("about page")
    return render(request,"app1/about.html")


def contact(request):
    print("request page")
    return render(request,"app1/contact.html")