from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from home.context_processors import hasGroup
from all_cases.models import case
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import bill
# Create your views here.
@login_required
def view_bills(request):
    c = {}
    c.update(csrf(request))
    if hasGroup(request.user, 'Patient'):
        c['bills'] = []
        c['isPatient'] = True
        for cases in case.objects.filter(patient=request.user):
            c['bills'].extend(list(bill.objects.filter(case=cases)))
    elif hasGroup(request.user, 'Receptionist'):
        
        c['isreceptionist']=True
        c['bills'] = []
        for cases in case.objects.all():
            c['bills'].extend(list(bill.objects.filter(case=cases)))
    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/home')

    bills = c['bills']
    c['paidBills'] = []
    c['pendingBills'] = []
    for b in bills:
        if b.is_paid:
            c['paidBills'].append(b)
        else:
            c['pendingBills'].append(b)
    return render(request, 'bills/view_bills.html', c)