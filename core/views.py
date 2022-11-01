from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    if (request.method == "POST"):
        name = request.POST["name"]
        message = request.POST["message"]
        email = request.POST["email"]
        print(name, message, email)
    return render(request, "contact.html")
