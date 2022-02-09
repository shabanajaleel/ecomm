from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages

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