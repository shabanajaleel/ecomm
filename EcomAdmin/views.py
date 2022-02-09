from django.shortcuts import render,redirect
from django.http import JsonResponse
from . forms import *
from EcomUser.models import Feedback
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.

def home(request):
    return render(request,'home.html')

def fnaddrole(request):
    form=AdminRoleForm()
    context={'form':form}
    return render(request,'admins/role/add_role.html',context)

def fnfeedback(request):
    feedback=Feedback.objects.all()
    print([i for i in feedback])
    context={'feedback':feedback}

    return render(request,'feedback/feedback.html',context)

# def fnfeedbackreply(request,feed_id):
#     if request.method=="POST":
#         email_to=request.POST['email_to']
#         subject=request.POST['subject']
#         message=request.POST['message']
#         email_from=settings.EMAIL_HOST_USER
#         send=send_mail(subject, message, email_from, [email_to] )
#         if send:
#             messages.success(request,"email sent successfully")

#     feedback=Feedback.objects.get(id=feed_id)
    
    
#     context={'data':feedback}
#     return render(request,'feedback/feedback_reply.html',context)


# def fnaddbanner(request):
#     form=BannerForm()
#     context={'form':form}
#     return render(request,'banners/addbanner.html',context)

def fnbrand(request):
    brands=Brand.objects.all()
    context={'brand':brands}
    return render(request,'brands/brands.html',context)

def fnaddbrand(request):
    
    if request.method=='POST':
        form=BrandForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        else:return render(request,'brands/addbrand.html',{'form':form})
    form=BrandForm()
    context={'form':form}
    return render(request,'brands/addbrand.html',context)

def fneditbrand(request,brand_id):
    brands=Brand.objects.get(id=brand_id)
    print(brands)
    form = BrandForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=brands)
    if form.is_valid():
          form.save()
          return redirect(fnbrand)
    return render(request, 'brands/updatebrand.html', {'form': form})

def fndisablebrand(request,branddis_id):
    brands=Brand.objects.get(id=branddis_id)
    if brands.status == 'active':
        brands.status ='inactive'
        brands.save()
        return redirect(fnbrand)
    else:
        brands.status ='active'
        brands.save()
        return redirect(fnbrand)



def fnaddcatogory(request):
    
    form=CatogoryForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Catogory inserted successfully')
    form=CatogoryForm()
    context={'form':form}
    return render(request,'catogory/addcatogory.html',context)

def fncatogory(request):
    catogories=Catogory.objects.all()
    context={'cat':catogories}
    return render(request,'catogory/catogories.html',context)

def fneditcatogory(request,cat_id):
    catogories=Catogory.objects.get(id=cat_id)
    form =CatogoryForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=catogories,
    )
    if form.is_valid():
        form.save()
        messages.success(request,'Catogory updated successfully')

    
    return render(request,'catogory/addcatogory.html',{'form':form})

def fndisablecatogory(request,catdis_id):
    catogories=Catogory.objects.get(id=catdis_id)
    if catogories.status== "active":
        catogories.status ='inactive'
        catogories.save()
        return redirect(fncatogory)
    else:
        catogories.status ='active'
        catogories.save()
        return redirect(fncatogory)

def fndisplay(request):

    data = request.GET.get('p')
    if int(data) in [i.display_order for i in Catogory.objects.all()]:
        data = True
    else:
        data = False
    return JsonResponse({'data':data})



def fnaddvarienttype(request):
    if request.method=="POST":
        form=VarientTypeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Varient Type inserted successfully")
    form=VarientTypeForm()
    context={'form':form}
    return render(request,'varients/varienttype/addvarienttype.html',context)

def fnvarienttype(request):
    varienttype=VarientType.objects.all
    context={'varienttype':varienttype}
    return render(request,'varients/varienttype/varienttype.html',context)

def fneditvarienttype(request,var_id):
    varienttypes=VarientType.objects.get(id=var_id)
    form=VarientTypeForm(request.POST or None,instance=varienttypes)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Type updated successfully')
    context={'form':form}

    return render(request,'varients/varienttype/addvarienttype.html',context)

def fndisablevarienttype(request,vardis_id):
    varienttypes=VarientType.objects.get(id=vardis_id)
    if varienttypes.status=="active":
        varienttypes.status='inactive'
        varienttypes.save()
        varientvalues=VarientValues.objects.filter(varient_type_id=varienttypes.id)
        for i in varientvalues:
            i.status="inactive"
            i.save()
        return redirect(fnvarienttype)
    else:
        varienttypes.status ="active"
        varienttypes.save()
        varientvalues=VarientValues.objects.filter(varient_type_id=varienttypes.id)
        for i in varientvalues:
            i.status="active"
            i.save()
        return redirect(fnvarienttype)


# Varient Values
def fnaddvarientvalues(request):
    if request.method=="POST":
        form=VarientValuesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Varient Type inserted successfully")
    form=VarientValuesForm()
    context={'form':form}
    return render(request,'varients/varientvalues/addvarientvalues.html',context)

def fnvarientvalues(request):
    varientvalues=VarientValues.objects.filter(status="active")
    context={'varientvalues':varientvalues}
    return render(request,'varients/varientvalues/varientvalues.html',context)

def fneditvarientvalues(request,varval_id):
    varientvalues=VarientValues.objects.get(id=varval_id)
    form=VarientValuesForm(request.POST or None,instance=varientvalues)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Values updated successfully')
    context={'form':form}

    return render(request,'varients/varientvalues/addvarientvalues.html',context)

def fndisablevarientvalues(request,disval_id):
    varientvalues=VarientValues.objects.get(id=disval_id)
    print(varientvalues)
    varientvalues.status ='inactive'
    varientvalues.save()
    return redirect(fnvarientvalues)

def fnvarientdisplay(request):
    data = request.GET.get('order')
    if int(data) in [i.display_order for i in VarientType.objects.all()]:
        data = True
    else:
        data = False
    return JsonResponse({'data':data})
    
# ---- end of varient values----


# Offers
def fnaddoffers(request):
    if request.method=="POST":
        form=OffersForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'Offers inserted successfully')
        else:
            
            return render(request,'offers/addoffers.html',{'form':form})

    form=OffersForm()
    context={'form':form}
    return render(request,'offers/addoffers.html',context)

def fnoffers(request):
    offers=Offers.objects.all()
    context={'offers':offers}
    return render(request,'offers/offers.html',context)

def fneditoffers(request,off_id):
    offers=Offers.objects.get(id=off_id)
    form =OffersForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=offers,
    )
    if form.is_valid():
        form.save()
        messages.success(request,'Offers updated successfully')
    return render(request,'offers/addoffers.html',{'form':form})

def fndisableoffers(request,offdis_id):
    offers=Offers.objects.get(id=offdis_id)
    if offers.status== "active":
        offers.status ='inactive'
        offers.save()
        return redirect(fnoffers)
    else:
        offers.status ='active'
        offers.save()
        return redirect(fnoffers)


   



