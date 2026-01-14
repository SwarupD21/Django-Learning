from django.shortcuts import render
from django.http import HttpResponse
from .models import Content,Store
from .forms import ChaiVarityForm

# Create your views here.

#localhost: 8000/firstapp
def journey(request):
    # return HttpResponse("Hello im back")
    menu = Content.objects.all()
    return render(request,'firstapp/index2.html',{'menu':menu})

def chai_store(request):
    stores = None
    if request.method == 'POST':
        form  = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(cai_varity = chai_varity)
    else:
        form = ChaiVarityForm()
    return render(request,'firstapp/stores.html',{'stores':stores,'form':form})