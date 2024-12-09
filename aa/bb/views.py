from django.shortcuts import render
from .models import *
# Create your views here.
def cv(request):
    cvv = cview.objects.all()
    return render(request,'CV.html',{'a':cvv})

def sname(request):
    s = request.GET.get('name','')
    f = cview.objects.filter(cname=s)
    return render(request,'sname.html',{'b':f})