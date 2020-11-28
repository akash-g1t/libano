from django.shortcuts import render, redirect
from .models import Address
from .forms import BankingForm

def index(request):
    if request.method == 'POST':
        form = BankingForm(request.POST)
        if form.is_valid():
            form.save()
            msg = True
            return render(request, 'banking/index.html', { 'form': BankingForm(), 'msg': msg})
    
    else:
        form = BankingForm()
        msg = False
    
    address = Address.objects.all().first()
    context = {
        'form': form,
        'msg': msg,
        'address': address
    }
    return render(request, 'banking/index.html', context)