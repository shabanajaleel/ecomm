from django.shortcuts import render,redirect
from django.http import JsonResponse
from . forms import *
from django.db.models import Q
from EcomUser.models import Feedback
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,get_user_model,update_session_auth_hash
from . filters import OrderDetailsFilter

User=get_user_model()
# Create your views here.
def fnhaspermission(request):
    loginuser=request.user.is_superuser
    print(loginuser)
    if loginuser == False:
        role=User.objects.get(username=request.user).role
        permissions=AdminRole.objects.get(role_name=role).permissions.all()
        perm=[i.path_name for i in permissions]
        return perm
    


@login_required(login_url="/admin/login/")
def home(request):
    return render(request,'home.html')


def fnlogin(request):
    if request.method=="POST":
        uname=request.POST['uname']
        password=request.POST['password']
        user=authenticate(username=uname,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
    return render(request,'login.html')

@login_required(login_url="/admin/login/")
def fnlogout(request):
    logout(request)
    return redirect(fnlogin)

@login_required(login_url="/admin/login/")
def fnchangepassword(request):
    if request.method=="POST":
        form=ChangePasswordForm(user=request.user,data=request.POST )
        print(form)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'password changed successfully')
    form=ChangePasswordForm(request.user)
    print(request.user)
    return render(request,'changepassword.html',{'form':form})



@login_required(login_url="/admin/login/")
def fnrole(request):
    roles=AdminRole.objects.all()
    context={'roles':roles}
    if request.method=="POST":
        role=request.POST['role']
        status=request.POST['status']
        if role:
            roles=roles.filter(role_name=role)
            context={'roles':roles}
        if status:
            roles=roles.filter(status=status)
            context={'roles':roles}
    return render(request,'admins/role/roles.html',context)

@login_required(login_url="/admin/login/")
def fnaddrole(request):
    if request.method=="POST":
        form=AdminRoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Admin Role added successfully')
            return redirect(fnrole)
            
        else:
            return render(request,'admins/role/add_role.html',{'form':form})
    form=AdminRoleForm()
    context={'form':form}
    return render(request,'admins/role/add_role.html',context)

@login_required(login_url="/admin/login/")
def fneditrole(request,role_id):
    roles=AdminRole.objects.get(id=role_id)
    form =AdminRoleForm(
    data=(request.POST or None),
    instance=roles,
    )
    if form.is_valid():
        form.save()
        messages.success(request,'Roles edited successfully')
        return redirect(fncatogory)

    return render(request,'admins/role/add_role.html',{'form':form})

@login_required(login_url="/admin/login/")
def fndisablerole(request,roledis_id):
    roles=AdminRole.objects.get(id=roledis_id)
    if roles.status== "Active":
        roles.status ='Inactive'
        roles.save()
        return redirect(fnrole)
    else:
        roles.status ='Active'
        roles.save()
        return redirect(fnrole)

@login_required(login_url="/admin/login/")
def fnsetpermission(request,per_id):
    if request.method=="POST":
        perm=request.POST.getlist('sub_perm')
        print(perm)
        addperm=AdminRole.objects.get(id=per_id)
        print( addperm.permissions)
        for i in perm:
            addperm.permissions.add(SubPath.objects.get(id=i))
        messages.success(request,'permissions added successfully')
        return redirect(fnaddrole)
    permission=[i.id for i in  AdminRole.objects.get(id=per_id).permissions.all()]
    print(permission)
    path=MainPath.objects.all()
    return render(request,'admins/role/addpermissions.html',{'path':path,'permission':permission})



def fnfeedback(request):
    feedback=Feedback.objects.all()
    print([i for i in feedback])
    context={'feedback':feedback}

    return render(request,'feedback/feedback.html',context)

@login_required(login_url="/admin/login/")
def fnaddadmin(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        print(form)
        if form.is_valid():
            user=form.save()
            messages.success(request,'data inserted successfully')
            return redirect(fnaddadmin)
        else:
            return render(request,'admins/admin/addadmin.html',{'form':form})
    return render(request,'admins/admin/addadmin.html',{'form':form})

@login_required(login_url="/admin/login/")
def fnviewadmin(request):
    admin=User.objects.all()
    context={'admin':admin}
    return render(request,'admins/admin/viewadmin.html',context)

@login_required(login_url="/admin/login/")
def fneditadmin(request,editadminid):
    admin=User.objects.get(id=editadminid)
    form =EditUserForm(request.POST or None,instance=admin)
    print(form)
    if form.is_valid():
        form.save()
        messages.success(request,'Admin edited successfully')
        return redirect(fnviewadmin)
    return render(request,'admins/admin/editadmin.html',{'form':form})


@login_required(login_url="/admin/login/")
def fndisableadmin(request,disadminid):
    admin=User.objects.get(id=disadminid)
    if admin.status== "Active":
        admin.status ='Inactive'
        admin.save()
        return redirect(fnviewadmin)
    else:
        admin.status ='Active'
        admin.save()
        return redirect(fnviewadmin)

@login_required(login_url="/admin/login/")
def fnaddpath(request):
    if request.method=="POST":
        form=MainPathForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Path added successfully')
            return redirect(fnaddpath)
            
        else:
            return render(request,'admins/path/add_main_path.html',{'form':form})
    form=MainPathForm()
    context={'form':form}
    return render(request,'admins/path/add_main_path.html',context)

@login_required(login_url="/admin/login/")
def fnmainpath(request):
    path=MainPath.objects.all()
    context={'path':path}
    if request.method=="POST":
        path=request.POST['path']
        status=request.POST['status']
        if path:
            roles=roles.filter(role_name=path)
            context={'roles':roles}
        if status:
            roles=roles.filter(status=status)
            context={'roles':roles}
    return render(request,'admins/path/add_main_path.html',context)

@login_required(login_url="/admin/login/")
def fnaddsubpath(request):
    if request.method=="POST":
        form=SubPathForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Path added successfully')
            return redirect(fnaddsubpath)
            
        else:
            return render(request,'admins/path/add_sub_path.html',{'form':form})
    form=SubPathForm()
    context={'form':form}
    return render(request,'admins/path/add_sub_path.html',context)

def fnmainpath(request):
    pass 

def fnsubpath(request):
    pass


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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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


@login_required(login_url="/admin/login/")
def fnaddcatogory(request):
    
    form=CatogoryForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Catogory added successfully')
        return redirect(fncatogory)
    form=CatogoryForm()
    context={'form':form}
    return render(request,'catogory/addcatogory.html',context)

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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


@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
def fneditvarienttype(request,var_id):
    varienttypes=VarientType.objects.get(id=var_id)
    form=VarientTypeForm(request.POST or None,instance=varienttypes)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Type updated successfully')
        return redirect(fnvarienttype)
    context={'form':form}

    return render(request,'varients/varienttype/addvarienttype.html',context)

@login_required(login_url="/admin/login/")
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
@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
def fneditvarientvalues(request,varval_id):
    varientvalues=VarientValues.objects.get(id=varval_id)
    form=VarientValuesForm(request.POST or None,instance=varientvalues)
    if form.is_valid():
        form.save()
        messages.success(request,'Varient Values changed successfully')
        return redirect(fnvarientvalues)
    context={'form':form}

    return render(request,'varients/varientvalues/addvarientvalues.html',context)

@login_required(login_url="/admin/login/")
def fndisablevarientvalues(request,disval_id):
    varientvalues=VarientValues.objects.get(id=disval_id)
    if varientvalues.status=="active":
        varientvalues.status='inactive'
        varientvalues.save() 
    else:
        varientvalues.status ="active"
        varientvalues.save()
    return redirect(fnvarientvalues)

@login_required(login_url="/admin/login/")
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
@login_required(login_url="/admin/login/")
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


@login_required(login_url="/admin/login/")
def fnoffers(request):
    if request.user.is_superuser:
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

    elif 'View Offers' in fnhaspermission(request) and  'Add Offers' in fnhaspermission(request) :
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
    else:
        messages.error(request,'You dont have access to this page')
        return render(request,'messages.html')

   
    return render(request,'offers/offers.html',context)

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
def fndisablearea(request,disarea_id):
    areas=Area.objects.get(id=disarea_id)
    if areas.status=="Active":
        areas.status='Inactive'
        areas.save() 
    else:
        areas.status ="Active"
        areas.save()
    return redirect(fnareas)

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
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

@login_required(login_url="/admin/login/")
def fnorders(request):
    orders=OrderDetails.objects.all()
    context={'orders':orders}
    if request.method=="POST":
        customer=request.POST['customer']
        orderstatus=request.POST['orderstatus']
        paymentstatus=request.POST['paystatus']
        fromdate=request.POST['fromdate']
        todate=request.POST['todate']
        if customer:
            orders=orders.filter(Q(customer__username=customer))
            context={'orders':orders}
        if orderstatus:
            orders=orders.filter(Q(order_status=orderstatus))
            context={'orders':orders}
        if paymentstatus:
            orders=orders.filter(Q(payment_status=paymentstatus))
            context={'orders':orders}
        if fromdate:
            orders=orders.filter(Q(order_date__gte=fromdate))
            context={'orders':orders}
        if todate:
            orders=orders.filter(Q(order_date__lte=todate))
            context={'orders':orders}
    
    return render(request,'orders/order.html',context)

    




   



