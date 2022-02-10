from django.shortcuts import render,redirect
from django.http import JsonResponse
from . forms import *
from django.db.models import Q
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
    if request.method=="POST":
        brand=request.POST['brand']
        status=request.POST['status']
        if brand:
            brands=Brand.objects.filter(brand_name=brand)
            context={'brand':brands}
        if status:
            brands=Brand.objects.filter(status=status)
            context={'brand':brands}
        if brand and status:
            brands=Brand.objects.filter(brand_name=brand,status=status)
            context={'brand':brands}

    
    return render(request,'brands/brands.html',context)

def fnaddbrand(request):
    
    if request.method=='POST':
        form=BrandForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'Brand added successfully')
            return redirect(fnbrand)
        else:
            return render(request,'brands/addbrand.html',{'form':form})
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
          messages.success(request,'Brand edited successfully')
          return redirect(fnbrand)
    return render(request, 'brands/addbrand.html', {'form': form})

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
        messages.success(request,'Catogory added successfully')
        return redirect(fncatogory)
    form=CatogoryForm()
    context={'form':form}
    return render(request,'catogory/addcatogory.html',context)

def fncatogory(request):
    catogories=Catogory.objects.all()
    context={'cat':catogories}
    if request.method=="POST":
        catogory=request.POST['catogory']
        parent=request.POST['parent']
        status=request.POST['status']

        if catogory:
            catogories=Catogory.objects.filter(catogory_name__icontains=catogory)
            context={'cat':catogories}
        if parent:
            catogories=Catogory.objects.filter(parent__catogory_name=parent)
            context={'cat':catogories}
        if status:
            catogories=Catogory.objects.filter(status=status)
            context={'cat':catogories}
        # if catogory or status or parent:
        #     catogories=Catogory.objects.filter(Q(catogory_name__icontains=catogory)|Q(parent__catogory_name__icontains=parent)|Q(status=status))
        #     context={'cat':catogories}

        if catogory and status and parent:
            catogories=Catogory.objects.filter(catogory_name__icontains=catogory,parent__catogory_name__icontains=parent,status=status)
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
        messages.success(request,'Catogory edited successfully')
        return redirect(fncatogory)

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
            messages.success(request,"Varient Type added successfully")
            return redirect(fnvarienttype)
    form=VarientTypeForm()
    context={'form':form}
    return render(request,'varients/varienttype/addvarienttype.html',context)

def fnvarienttype(request):
    varienttype=VarientType.objects.all
    context={'varienttype':varienttype}
    if request.method=="POST":
        varient=request.POST['varienttype']
        status=request.POST['status']
        if varient:
            varienttype=VarientType.objects.filter(varient_name=varient)
            context={'varienttype':varienttype}
        if status:
            varienttype=VarientType.objects.filter(status=status)
            context={'varienttype':varienttype}
        if varient and status:
            varienttype=VarientType.objects.filter(varient_name=varient,status=status)
            context={'varienttype':varienttype}

    return render(request,'varients/varienttype/varienttype.html',context)

def fneditvarienttype(request,var_id):
    varienttypes=VarientType.objects.get(id=var_id)
    form=VarientTypeForm(request.POST or None,instance=varienttypes)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Type updated successfully')
        return redirect(fnvarienttype)
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
            messages.success(request,"Varient Type iadded successfully")
            return redirect(fnvarientvalues)
    form=VarientValuesForm()
    context={'form':form}
    return render(request,'varients/varientvalues/addvarientvalues.html',context)

def fnvarientvalues(request):
    varientvalues=VarientValues.objects.all()
    context={'varientvalues':varientvalues}
    if request.method=="POST":
        varientvals=request.POST['varientvalue']
        varient=request.POST['varienttype']
        status=request.POST['status']
        if varientvals:
            varientvalues=VarientValues.objects.filter(varient_values=varientvals)
            context={'varientvalues':varientvalues}
        if varient:
            varientvalues=VarientValues.objects.filter(varient_type__varient_name=varient)
            context={'varientvalues':varientvalues}
        if status:
            varientvalues=VarientValues.objects.filter(status=status)
            context={'varientvalues':varientvalues}
        if varient and status and varientvals:
            varientvalues=VarientValues.objects.filter(varient_values=varientvals,status=status,varient_type=varient)
            context={'varientvalues':varientvalues}
    return render(request,'varients/varientvalues/varientvalues.html',context)

def fneditvarientvalues(request,varval_id):
    varientvalues=VarientValues.objects.get(id=varval_id)
    form=VarientValuesForm(request.POST or None,instance=varientvalues)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Values changed successfully')
        return redirect(fnvarientvalues)
    context={'form':form}

    return render(request,'varients/varientvalues/addvarientvalues.html',context)

def fndisablevarientvalues(request,disval_id):
    varientvalues=VarientValues.objects.get(id=disval_id)
    if varientvalues.status=="active":
        varientvalues.status='inactive'
        varientvalues.save() 
    else:
        varientvalues.status ="active"
        varientvalues.save()
    return redirect(fnvarientvalues)

def fnvarientdisplay(request):
    data = request.GET.get('order')
    if int(data) in [i.display_order for i in VarientType.objects.all()]:
        data = True
    else:
        data = False
    return JsonResponse({'data':data})

def fnvarientvaluesdisplay(request):
    data = request.GET.get('order')
    if int(data) in [i.display_order for i in VarientValues.objects.all()]:
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
            messages.success(request,'Offers added successfully')
            return redirect(fnoffers)
        else:
            
            return render(request,'offers/addoffers.html',{'form':form})

    form=OffersForm()
    context={'form':form}
    return render(request,'offers/addoffers.html',context)

def fnoffers(request):
    offers=Offers.objects.all()
    context={'offers':offers}
    if request.method=="POST":
        offer=request.POST['offer']
        status=request.POST['status']
        if offers or status:
            offers=Offers.objects.filter(Q(offer_name=offer) | Q(status=status))
            context={'offers':offers}
        if offers and status:
            offers=Offers.objects.filter(offer_name=offer,status=status)
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
        messages.success(request,'Offers edited successfully')
        return redirect(fnoffers)
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


def fnareas(request):
    areas=Area.objects.all()
    context={'areas':areas}
    return render(request,'area/areas.html',context)


def fnaddarea(request):
    if request.method=="POST":
        form=AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Area inserted successfully")
            return redirect(fnareas)
    form=AreaForm()
    context={'form':form}
    return render(request,'area/addarea.html',context)

def fnaddpincode(request,pin_id):
    if request.method=="POST":
        form=PincodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'pincode inserted successfully')
   
    form=PincodeForm(initial={'area':pin_id})
    pin=Pincode.objects.filter(area=pin_id)
    context={'form':form,'pin':pin}

    return render(request,'area/addpincode.html',context)

def fndisablearea(request,disarea_id):
    areas=Area.objects.get(id=disarea_id)
    if areas.status=="Active":
        areas.status='Inactive'
        areas.save() 
    else:
        areas.status ="Active"
        areas.save()
    return redirect(fnareas)

def fndisablepincode(request,dispin_id):
    pincode=Pincode.objects.get(id=dispin_id)
    pin_id=pincode.area
    if pincode.status=="Active":
        pincode.status='Inactive'
        pincode.save() 
    else:
        pincode.status ="Active"
        pincode.save()
    return redirect(fnareas)

def fneditareas(request,editarea_id):
    areas=Area.objects.get(id=editarea_id)
    form =AreaForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=areas,
    )
    if form.is_valid():
        form.save()
        messages.success(request,'Areas Changed successfully')
        return redirect(fnareas)
    return render(request,'area/addarea.html',{'form':form})

# def fneditpincode(request,editpin_id):
#     pincode=Pincode.objects.get(id=editpin_id)
#     form =PincodeForm(
#     data=(request.POST or None),
#     files=(request.FILES or None),
#     instance=pincode,
#     )
#     if form.is_valid():
#         form.save()
#         messages.success(request,'Pincode edited successfully')
#         return redirect(fnoffers)
#     return render(request,'offers/addoffers.html',{'form':form})


    




   



