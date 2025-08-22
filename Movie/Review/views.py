from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Departments,About
from .models import Doctors,Contact
# Create your views here.
def  index(request):
    return render(request,'index.html')
def  base(request):
    return render(request,'base.html')

def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Confirmation.html')
    form = BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    dict_dept ={
        'dept':Contact.objects.all()
    }
    return render(request,'contact.html',dict_dept)


def department(request):
    dict_dept ={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
def about(request):
    dict_abt={
        'abt':About.objects.all()
    }
    return render(request,'about.html',dict_abt)