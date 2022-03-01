from django.shortcuts import render,redirect
from . forms import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from EcomAdmin.models import Banners,Catogory,Brand,Product,Customer
from EcomAdmin.forms import CustomerForm
from django.contrib.auth.decorators import user_passes_test


def login_required_custom(request):
    if 'customer' in request.session:
        return True

def fnhome(request):
    products=Product.objects.all()
    brands=Brand.objects.all()
    catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
    allcatogory=Catogory.objects.filter(status="Active")
    banners=Banners.objects.all()

    if 'customer' in request.session:
        currentUser=request.session['customer']
        context={'banner':banners,'catogory': catogory,'brand':brands,'allcat':allcatogory,'products':products,'currentUser':currentUser}
        return render(request,'index.html',context)
    context={'banner':banners,'catogory': catogory,'brand':brands,'allcat':allcatogory,'products':products}
    return render(request,'index.html',context)

def fnregister(request):
    if request.method=="POST":
        form=CustomerForm(request.POST or None)
        if form.is_valid():
            register=form.save(commit=False)
            password=form.cleaned_data['password']
            conf_password=form.cleaned_data['conf_password']
            newpassword=make_password(password, salt=None, hasher='default')
            newconfpassword=make_password(conf_password, salt=None, hasher='default')
            register.password=newpassword
            register.conf_password=newconfpassword
            register.save()
            messages.success(request,'Successfully signed in..')
            return redirect(fnlogin)
        else:
            return render(request,'user_login.html',{'form':form})

def fnchangeuserpassword(request):
    currentUser=request.session['customer']
    if request.method=="POST":
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']
        retype_password=request.POST['retype_password']
        customer=Customer.objects.get(id=currentUser)
        old_hashed_password=check_password(old_password,customer.password)
        if old_hashed_password == True:
            new_hashed_password=make_password(new_password,salt=None, hasher='default')
            retype_hashed_password=make_password(retype_password,salt=None, hasher='default')
            customer.password=new_hashed_password
            customer.conf_password=retype_hashed_password
            customer.save()
            messages.success(request,'password changed successfully')
            return render(request,'changeUserPassword.html',{'currentUser':currentUser})
        else:
            messages.error(request,'Invalid Password')
            return render(request,'changeUserPassword.html',{'currentUser':currentUser})

    return render(request,'changeUserPassword.html',{'currentUser':currentUser})




def fnlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        customer=Customer.objects.get(username=username,email=email)
        enc_password=check_password(password,customer.password)
        if enc_password==True:
            request.session['customer']=customer.id
            print(request.session['customer'])
            return redirect(fnhome)
    form=CustomerForm()
    context={'form':form}
    return render(request,'user_login.html',context)

def fnlogout(request):
    print(request.session['customer'])
    del request.session['customer']
    return redirect(fnhome)


def fnwishlist(request):
    return render(request,'wishlists.html')

def fncart(request):
    return render(request,'cart.html')


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