from django.shortcuts import render
from . forms import *
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your views here.
def start_view(request):
    return render(request,'register/start.html')

def pregister_view(request):
    form=RegisterForm(request.POST or None)
    context={}
    if form.is_valid():
        form.save()
        return redirect('/register_patient')
    context['form']=form
    return render(request,'register/register.html',context)

def dregister_view(request):
    form=RegisterForm(request.POST or None)
    context={}
    if form.is_valid():
        form.save()
        return redirect('/register_doctor')
    context['form']=form
    return render(request,'register/register.html',context)

def registerp_view(request):
    context={};
    form=PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        user=form.cleaned_data['user']
        groupname ,created=Group.objects.get_or_create(name='Patient')
        # try:
        #     user = User.objects.get(username=myusername)
        # except:
        #     user= None
        if user is not None:
            groupname.user_set.add(user)
        return redirect('/login')
    context['form']=form

    return render(request,'register/create_patient.html',context)

def registerd_view(request):
    context={};
    form=DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        user=form.cleaned_data['user']
        groupname ,created=Group.objects.get_or_create(name='Doctor')
        # try:
        #     user = User.objects.get(username=myusername)
        # except:
        #     user= None
        if user is not None:
            groupname.user_set.add(user)
        return redirect('/login')
    context['form']=form

    return render(request,'register/create_doctor.html',context)