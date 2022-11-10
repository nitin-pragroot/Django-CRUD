from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Student
from .forms import StudentData
from django.http import HttpResponse
# Create your views here.


def Insert(request):
    return render(request,"insert.html")

def InsertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    return redirect("showpage")

def Showpage(request):
    all_data = Student.objects.all()
    return render(request,"show.html",{'key1':all_data})

def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname=request.POST['fname']
    udata.Lastname=request.POST['lname']
    udata.Email=request.POST['email']
    udata.Contact=request.POST['contact']
    udata.save()
    return redirect('showpage')

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')
