from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from home.context_processors import hasGroup

# Create your views here.
@login_required
def home(request):
    context={}
    context['ispatient']=False
    context['isdoctor']=False
    context['isreceptionist']=False
    context['ishr']=False
    if hasGroup(request.user, 'Patient'):
        context['ispatient']=True
    if hasGroup(request.user, 'Doctor'):
        context['isdoctor']=True
    if hasGroup(request.user, 'Receptionist'):
        context['isreceptionist']=True
    if hasGroup(request.user, 'HR'):
        context['ishr']=True

    return render(request, 'home/home.html',context)