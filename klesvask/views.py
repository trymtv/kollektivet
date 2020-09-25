from django.shortcuts import render, redirect
from datetime import timedelta
from .models import Wash, WashQueue
from django.utils import timezone
from .forms import RegWash, RegQueue
from django.contrib import messages
from django.core.mail import send_mail
from django.core.management import call_command

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def index(request):
    if Wash.objects.last():
        call_command('checkwash')
        lastWash = Wash.objects.last()
        if lastWash.ongoing:
            return render(request, 'klesvask/vasker.html', {'title':'Klesvask',
                'endTime':(lastWash.endTime + timedelta(minutes = 1, hours=2)).strftime('%H:%M'),
                'centerContent':True,
                'washQueue':WashQueue.objects.all(),
                'washForm':RegQueue})
    return render(request, 'klesvask/vasker.html', {'title':'Klesvask', 'centerContent':True, 'washQueue':WashQueue.objects.all(),'washForm':RegQueue})

def regWash(request):
    if not Wash.objects.last().ongoing:
        if request.method == 'POST':
            form = RegWash(request.POST)
            if form.is_valid():
                formWashType = form.cleaned_data['washType']
                formDegrees = form.cleaned_data['degrees']
                formWashLength = form.cleaned_data['washLength']
                formEndTime = timezone.now() + timedelta(minutes=form.cleaned_data['washLength'])
                regWash = Wash(user=request.user, washType=formWashType, degrees=formDegrees, washLength=formWashLength, endTime=formEndTime, ongoing=True)
                regWash.save()
                messages.add_message(request, messages.SUCCESS, 'Vasken ble registrert!')
                if formWashType == 'ullvask' and formDegrees > 30:
                    messages.add_message(request, messages.INFO, 'Vaske ull så varmt?! Er du dum eller?')
                return redirect('/klesvask/')
            else:
                messages.add_message(request, messages.ERROR, 'Det ble skrevet noe ugyldig!')
        else:
            form = RegWash()
        return render(request, 'klesvask/reg_vask.html', {'title':'Klesvask', 'form':form})
    else:
        return redirect('/klesvask/')

def addToQueue(request):
    if request.method == 'POST':
        if not WashQueue.objects.filter(user=request.user):
            form = RegQueue(request.POST)
            if form.is_valid():
                WashQueue(user=request.user, washType=form.cleaned_data['washType']).save()
        else:
            WashQueue.objects.filter(user=request.user).delete()
    return redirect('/klesvask/')