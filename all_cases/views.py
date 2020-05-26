from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import case
from appointments.models import Appointment
from home.context_processors import hasGroup
from .forms import CaseForm
from django.shortcuts import redirect

# Create your views here.
@login_required
def view_cases(request):
    c = {}
    user = request.user
    cases = None
    if hasGroup(user, 'Receptionist'):
        cases = case.objects.all()
    elif hasGroup(user, 'Patient'):
        cases = case.objects.filter(patient=user)
    elif hasGroup(user, 'Doctor'):
        c['isDoctor'] = True
        cases = [appointment.case for appointment in Appointment.objects.filter(doctor=user)]

    open=[]
    closed=[]
    if cases is not None:
        for ca in cases:
            if ca.closed_date:
                closed.append(ca)
            else:
                open.append(ca)
        c['openCases'] = open
        c['closedCases'] = closed
    return render(request, 'case/view_cases.html', c)

@login_required
def new_case(request):
    form=CaseForm(request.POST or None)
    context={}
    if hasGroup(request.user, 'Receptionist'):
        context['isreceptionist']=True
    if form.is_valid():
        form.save()
        latest_case=case.objects.latest('id')
        return redirect('appointments:new_appointment')
    context['form']=form
    return render(request,'case/new_case.html',context)
    


