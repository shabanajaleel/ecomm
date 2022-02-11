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
            brands=brands.filter(brand_name=brand)
            context={'brand':brands}
        if status:
            brands=brands.filter(status=status)
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
            catogories=catogories.filter(catogory_name=catogory)
            context={'cat':catogories}
        if parent:
            catogories=catogories.filter(parent__catogory_name=parent)
            context={'cat':catogories}
        if status:
            catogories=catogories.filter(status=status)
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
    varienttype=VarientType.objects.all()
    context={'varienttype':varienttype}
    if request.method=="POST":
        varient=request.POST['varienttype']
        status=request.POST['status']
        if varient:
            varienttype=varienttype.filter(varient_name=varient)
            context={'varienttype':varienttype}
        if status:
            varienttype=varienttype.filter(status=status)
            context={'varienttype':varienttype}
        if varient and status:
            varienttype=varienttype.filter(varient_name=varient,status=status)
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
            varientvalues=varientvalues.filter(varient_values=varientvals)
            context={'varientvalues':varientvalues}
        if varient:
            varientvalues=varientvalues.filter(varient_type__varient_name=varient)
            context={'varientvalues':varientvalues}
        if status:
            varientvalues=varientvalues.filter(status=status)
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
        if offer:
            offers=offers.filter(Q(offer_name=offer))
            context={'offers':offers}
        if status:
            offers=offers.filter(Q(status=status))
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
    if request.method=="POST":
        area=request.POST['area']
        status=request.POST['status']
        if area:
            areas=areas.filter(Q(area_name=area))
            context={'areas':areas}
        if status:
            areas=areas.filter(status=status)
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

def fncustomers(request):
    customers=Customer.objects.all()
    context={'customers':customers}
    if request.method=="POST":
        customer=request.POST['user']
        status=request.POST['status']
        if customer:
            customers=customers.filter(Q(username=customer))
            context={'customers':customers}
        if status:
            customers=customers.filter(Q(status=status))
            context={'customers':customers}
    
    return render(request,'customer/customer.html',context)

def fndisablecustomer(request,customid):
    customer=Customer.objects.get(id=customid)
    if customer.status== 1 :
        customer.status=0
        customer.save()
        return redirect(fncustomers)
    if customer.status== 0 :
        customer.status=1
        customer.save()
        return redirect(fncustomers)

def fnaddbanner(request):
    if request.method=="POST":
        form=BannerForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'Banners added successfully')
            return redirect(fnmainbanner)
            
        else:
            return render(request,'banners/main/addbanner.html',{'form':form})

    form=BannerForm()
    context={'form':form}
    return render(request,'banners/main/addbanner.html',context)

def fnaddinnerbanner(request):
    if request.method=="POST":
        form=BannerForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            banner=form.save(commit=False)
            banner.is_intermediate=1
            banner.save()
            messages.success(request,'Intermediate Banners added successfully')
            return redirect(fninnerbanner)
            
        else:
            return render(request,'banners/intermediate/addinnerbanner.html',{'form':form})

    form=BannerForm()
    context={'form':form}
    return render(request,'banners/intermediate/addinnerbanner.html',context)

def fninnerbanner(request):
    innerbanners=Banners.objects.filter(is_intermediate=1)
    context={'innerbanners':innerbanners}
    if request.method=="POST":
        banner=request.POST['banner']
        URL=request.POST['URL']
        status=request.POST['status']
        if banner:
            innerbanners=innerbanners.filter(Q(banner_name=banner),Q(is_intermediate=1))
            context={'innerbanners':innerbanners}
        if URL:
            innerbanners=innerbanners.filter(Q(banner_url=URL),Q(is_intermediate=1))
            context={'innerbanners':innerbanners}
        if status:
            innerbanners=innerbanners.filter(Q(status=status),Q(is_intermediate=1))
            context={'innerbanners':innerbanners}

    return render(request,'banners/intermediate/innerbanner.html',context)

def fnmainbanner(request):
    innerbanners=Banners.objects.filter(is_intermediate=0)
    context={'innerbanners':innerbanners}
    if request.method=="POST":
        banner=request.POST['banner']
        URL=request.POST['URL']
        status=request.POST['status']
        if banner:
            innerbanners=innerbanners.filter(Q(banner_name=banner),Q(is_intermediate=0))
            context={'innerbanners':innerbanners}
        if URL:
            innerbanners=innerbanners.filter(Q(banner_url=URL),Q(is_intermediate=0))
            context={'innerbanners':innerbanners}
        if status:
            innerbanners=innerbanners.filter(Q(status=status),Q(is_intermediate=0))
            context={'innerbanners':innerbanners}
    return render(request,'banners/main/mainbanner.html',context)

def fnmaindisplay(request):
    data = request.GET.get('p')
    if int(data) in [i.display_order for i in Banners.objects.filter(is_intermediate=0)]:
        data = True
    else:
        data = False
    return JsonResponse({'data':data})

def fninnerdisplay(request):
    data = request.GET.get('p')
    if int(data) in [i.display_order for i in Banners.objects.filter(is_intermediate=1)]:
        data = True
    else:
        data = False
    return JsonResponse({'data':data})

def fneditinner(request,inneredit_id):
    innerbanner=Banners.objects.get(id=inneredit_id)
    form =BannerForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=innerbanner,
    )
    if form.is_valid():
        banner=form.save(commit=False)
        banner.is_intermediate=1
        banner.save()
        messages.success(request,'Intermediate Banners changed successfully')
        return redirect(fninnerbanner)
    return render(request,'banners/intermediate/addinnerbanner.html',{'form':form})

def fndisableinnerbanner(request,innerban_id):
    banner=Banners.objects.get(id=innerban_id)
    if banner.status== "Active" :
        banner.status='Inactive'
        banner.save()
        return redirect(fninnerbanner)
    else:
        banner.status="Active"
        banner.save()
        return redirect(fninnerbanner)

def fneditmain(request,mainedit_id):
    innerbanner=Banners.objects.get(id=mainedit_id)
    form =BannerForm(
    data=(request.POST or None),
    files=(request.FILES or None),
    instance=innerbanner,
    )
    if form.is_valid():
        form.save()
        messages.success(request,' Banners changed successfully')
        return redirect(fnmainbanner)
    return render(request,'banners/intermediate/addinnerbanner.html',{'form':form})

def fndisablemainbanner(request,mainban_id):
    banner=Banners.objects.get(id=mainban_id)
    if banner.status== "Active" :
        banner.status='Inactive'
        banner.save()
        return redirect(fnmainbanner)
    else:
        banner.status="Active"
        banner.save()
        return redirect(fnmainbanner)

    




   



