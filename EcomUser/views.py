from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from EcomAdmin.models import Banners,Catogory,Brand,Product


def fnhome(request):
    products=Product.objects.all()
    brands=Brand.objects.all()
    catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
    allcatogory=Catogory.objects.filter(status="Active")
    banners=Banners.objects.all()
    context={'banner':banners,'catogory': catogory,'brand':brands,'allcat':allcatogory,'products':products}
    return render(request,'usermain.html',context)

def fnfeedback(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            form.save()
            messages.success(request,"Data inserted successfully")
            return redirect(fnfeedback)
        else:
            return render(request,'feedback/contact.html',{'form':form})
        
    form=FeedbackForm()
    context={'form':form}
    return render(request,'feedback/contact.html',context)