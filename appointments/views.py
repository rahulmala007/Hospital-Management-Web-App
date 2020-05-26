from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.context_processors import hasGroup
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Appointment
from django.utils import timezone
from .forms import AppointmentForm
from django.shortcuts import redirect
# Create your views here.

#view_appointments
@login_required
def view_appointments(request):
    c = {}
    user = request.user
    c['isReceptionist'] = False
    if hasGroup(user, 'Receptionist'):
        c['isReceptionist'] = True
        c['upappointments'] = Appointment.objects.filter(appointment_time__gte=timezone.now()).order_by('appointment_time')
        c['ltappointments'] = Appointment.objects.filter(appointment_time__lt=timezone.now()).order_by('appointment_time')

    elif hasGroup(user, 'Patient'):
        c['upappointments'] = Appointment.objects.filter(patient=user, appointment_time__gte=timezone.now()).order_by('appointment_time')
        c['ltappointments'] = Appointment.objects.filter(patient=user, appointment_time__lt=timezone.now()).order_by('appointment_time')
    elif hasGroup(user, 'Doctor'):
        c['upappointments'] = Appointment.objects.filter(doctor=user, appointment_time__gte=timezone.now()).order_by('appointment_time')
        c['ltappointments'] = Appointment.objects.filter(doctor=user, appointment_time__lt=timezone.now()).order_by('appointment_time')

    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/home')
    return render(request, 'appointments/view_appointments.html', c)

@login_required
def new_appointment(request):
    form=AppointmentForm(request.POST or None)
    context={}
    if hasGroup(request.user, 'Receptionist'):
        context['isreceptionist']=True
    if form.is_valid():
        form.save()
        return redirect('home:dash')
    context['form']=form
    return render(request,'appointments/new_appointment.html',context)

@login_required
def update_appointment(request,id):
    instance=Appointment.objects.get(id=id)
    c={}
    c['isreceptionist']=False
    if hasGroup(request.user,'Receptionist'):
        c['isreceptionist']=True
    form=AppointmentForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home:dash')
    c['form']=form;
    return render(request,'appointments/update_appointment.html',c)

@login_required
def delete_appointment(request,id):
    instance=Appointment.objects.get(id=id)
    if instance is not None:
        instance.delete()
    return redirect('home:dash')