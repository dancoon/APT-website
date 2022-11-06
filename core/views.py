from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Contact
from .forms import ContactForm, MemberRegistrationForm


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            fname = cd.get("fname")
            lname = cd.get("lname")
            # message = cd.get["message"]
            Contact.objects.create(
                fname = fname,
                lname = lname,
            )
    return render(request, "contact.html", {'form':form})

def members(request):
    members = Member.objects.filter(is_active = True)
    
    form = MemberRegistrationForm()
    if (request.method == "POST"):
        if (form is _valid):
            form.save
    return render(request, "members.html", {'members': members, 'form': form})

