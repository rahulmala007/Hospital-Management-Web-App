from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from home.context_processors import hasGroup
from .models import *
from .forms import PatientForm,DoctorForm
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.views import generic
from django.shortcuts import redirect
from bills.models import bill
# Create your views here.

@login_required
def profile(request):
    context={}
    if hasGroup(request.user, 'Patient'):
        context['ispatient']=True
    else:
        context['ispatient']=False
    return render(request,'profiles/all_profiles.html',context);

@login_required
def new_patient(request):
    context={};
    context['isreceptionist']=False
    if hasGroup(request.user, 'Receptionist'):
        context['isreceptionist']=True
        form=PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
            new_user=User.objects.latest('id')
            return redirect('home:dash')
        context['form']=form

    return render(request,'profiles/create_patient.html',context)

@login_required
def register(request):
    form=RegisterForm(request.POST or None)
    context={}
    if hasGroup(request.user, 'Receptionist'):
        context['isreceptionist']=True
    if form.is_valid():
        form.save()
        form=RegisterForm()
        return redirect('profiles:new_patient')
    context['form']=form
    return render(request,'profiles/register.html',context)

@login_required
def hr_view(request):
    c = {}
    user = request.user
    c['isHR']=False
    if hasGroup(user, 'HR'):
        c['isHR']=True
        c['all_doctors']=Doctor.objects.all().order_by('id')
        c['on_duty']=Doctor.objects.filter(on_duty=True).order_by('id')
        c['off_duty']=Doctor.objects.filter(on_duty=False).order_by('id')
    return render(request,'profiles/hr_view.html',c)


@login_required
def hrpatient_view(request):
    c = {}
    user = request.user
    c['isHR']=False
    if hasGroup(user, 'HR'):
        c['isHR']=True
        c['all_patients']=Patient.objects.all().order_by('id')
    return render(request,'profiles/hrpatient_view.html',c)
    

@login_required
def hraccounnting_view(request):
    c = {}
    user = request.user
    c['isHR']=False
    if hasGroup(user, 'HR'):
        c['isHR']=True
        c['paid_bills']=bill.objects.filter(is_paid=True).order_by('bill_date')
        c['unpaid_bills']=bill.objects.filter(is_paid=False).order_by('bill_date')
    return render(request,'profiles/hraccounting_view.html',c)

@login_required   
def delete_patient(request,id):
    instance=Patient.objects.get(id=id)
    if instance is not None:
        instance.delete()
    return redirect('home:dash')

@login_required
def delete_doctor(request,id):
    instance=Doctor.objects.get(id=id)
    if instance is not None:
        instance.delete()
    return redirect('home:dash')

@login_required
def update_patient(request,id):
    instance=Patient.objects.get(id=id)
    c={}
    c['isHR']=False
    if hasGroup(request.user,'HR'):
        c['isHR']=True
    form=PatientForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home:dash')
    c['form']=form;
    return render(request,'profiles/update_patient.html',c)

@login_required
def update_doctor(request,id):
    instance=Doctor.objects.get(id=id)
    c={}
    c['isHR']=False
    if hasGroup(request.user,'HR'):
        c['isHR']=True
    form=DoctorForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home:dash')
    c['form']=form;
    return render(request,'profiles/update_doctor.html',c)



    


