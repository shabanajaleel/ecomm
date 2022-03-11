from random import randint
from django.http import JsonResponse
from django.shortcuts import render,redirect
from . forms import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from EcomAdmin.models import Banners,Catogory,Brand,Product,Customer,Product_Varients,CoupenCode
from EcomAdmin.forms import CustomerForm
from django.contrib.auth.decorators import user_passes_test
from . decorator import login_cart
from django.db.models import Sum
from django.db.models import F
from django.core.paginator import Paginator

# twilio
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# end twilio settings


# main context

context={}
context['catogory']=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
context['allcat']=Catogory.objects.filter(status="Active")

#end context 




def fnindex(request):
    return render(request,'newindex.html')

  
def login_required_custom(request):
    if 'customer' in request.session:
        return True

def fnhome(request):
    products=Product.objects.all()
    brands=Brand.objects.all()
    catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
    allcatogory=Catogory.objects.filter(status="Active")
    banners=Banners.objects.all()
    cart_count=0
    wish_count=0
    

    if 'customer' in request.session:
        currentUser=request.session['customer']
        cart_count=Cart.objects.filter(customer=currentUser).count()
        wish_count=Wishlist.objects.filter(customer=currentUser).count()
        context={'banner':banners,'catogory': catogory,'brand':brands,'allcat':allcatogory,'products':products,'currentUser':currentUser,'cart_count':cart_count,'wish_count':wish_count}
        return render(request,'newindex.html',context)

    context={'banner':banners,'catogory': catogory,'brand':brands,'allcat':allcatogory,'products':products,'cart_count':cart_count,'wish_count':wish_count}
    return render(request,'newindex.html',context)

def fnregister(request):
    form=CustomerForm()
    context={'form':form}
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
            return render(request,'user_register.html',{'form':form})
    return render(request,'user_register.html',context)

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
    if request.method=="POST":
        mobile=request.POST['mobile']
        password=request.POST['password']
        customer=Customer.objects.get(phone=mobile)
        enc_password=check_password(password,customer.password)
        if enc_password==True:
            mobile=customer.phone
            print(mobile)
            otp=str(randint(1000,9999))
            customer.otp=otp
            customer.save()
            request.session['customer']=customer.id
            message = client.messages \
                    .create(
                        body="Your OTP for login is " + otp,
                        from_='+19107765960',
                        to='+91' + str(mobile)
                    )
            if message:
                return render(request,'enter_otp.html')
            else:
                return render(request,'userlogin.html')


        else:
            messages.error(request,'Wrong Password...')
            return redirect(fnlogin)

    catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
    allcatogory=Catogory.objects.filter(status="Active")
    form=CustomerForm()
    context={'form':form,'catogory': catogory,'allcat':allcatogory}
    return render(request,'user_login.html',context)
    



def fnotplogin(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        customer=Customer.objects.get(username=username,email=email)
        if customer:
            mobile=customer.phone
            print(mobile)
            otp=str(randint(1000,9999))
            customer.otp=otp
            customer.save()
            request.session['customer']=customer.id
            message = client.messages \
                    .create(
                        body="Your OTP for login is " + otp,
                        from_='+19107765960',
                        to='+91' + str(mobile)
                    )
            if message:
                return render(request,'enter_otp.html')
            else:
                return render(request,'user_otp_login.html')


        else:
            messages.error(request,'invalid username or email')
            return redirect(fnotplogin)

    return render(request,'user_otp_login.html')

def fnenterotp(request):
    if request.method=="POST":
        otp=request.POST['otp']
        if request.session.has_key('customer'):
            user=request.session['customer']
            customer=Customer.objects.get(id=user)
            if otp==customer.otp :
                return redirect(fnhome)
            else:
                messages.error(request,'incorrect otp')
                return render(request,'enter_otp.html')

    return render(request,'enter_otp.html')

# login using password


# def fnlogin(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         customer=Customer.objects.get(username=username,email=email)
#         enc_password=check_password(password,customer.password)
#         if enc_password==True:
#             request.session['customer']=customer.id
#             print(request.session['customer'])
#             return redirect(fnhome)
#     catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
#     allcatogory=Catogory.objects.filter(status="Active")
#     form=CustomerForm()
#     context={'form':form,'catogory': catogory,'allcat':allcatogory}
#     return render(request,'user_login.html',context)

def fnlogout(request):
    print(request.session['customer'])
    del request.session['customer']
    return redirect(fnhome)


def fnwishlist(request):
    if request.method=="POST":
        currentUser=request.session['customer']
        varient=request.POST['varient_id']
        product=Product_Varients.objects.get(id=varient)
        check_wishlist=Wishlist.objects.filter(customer=currentUser,product=varient).exists()
        
        if check_wishlist== True:
            message="Product is already in Wishlist"
            return JsonResponse({'message':message})
        else:

            wishlist=Wishlist(customer_id=currentUser,product_id=varient,unit_price=product.Selling_Prize)
            wishlist.save()
            count=Wishlist.objects.filter(customer_id=currentUser).count()
            return JsonResponse({'count':count})

def fnviewwishlist(request):
    currentUser=request.session['customer']
    user_wishlist=Wishlist.objects.filter(customer_id=currentUser)
    cart_count=Cart.objects.filter(customer=currentUser).count()
    wish_count=Wishlist.objects.filter(customer=currentUser).count()
    context={'wishlist': user_wishlist,'cart_count':cart_count,'wish_count':wish_count}
    
    return render(request,'wishlists.html',context)

def fnremovewishlist(request):
    if request.method=="POST":
        currentUser=request.session['customer']
        id=request.POST['id']

        wishlist=Wishlist.objects.filter(product_id=id)
        if wishlist:
            wishlist.delete()
            message="Item removed from wishlist"
        return JsonResponse({'message':message})

# add to cart from wishlist 
def fnaddtocartwish(request):
     if request.method=="POST":
        currentUser=request.session['customer']

        qty=request.POST['qty']
# quantity must be checked later
        varient=request.POST['varient_id']
        product=Product_Varients.objects.get(id=varient)
        check_cart=Cart.objects.filter(customer=currentUser,product=varient).exists()
        
        if check_cart== True:
            message="Product is already in cart"
            return JsonResponse({'message':message})
        else:

            cart=Cart(customer_id=currentUser,product_id=varient,quantity=qty,selling_price=product.Selling_Prize,display_price=product.Display_Prize)
            cart.save()
            wishlist=Wishlist.objects.filter(customer_id=currentUser,product_id=varient)
            wishlist.delete()
            count=Cart.objects.filter(customer_id=currentUser).count()
            return JsonResponse({'count':count})


def fncart(request):
    if request.method=="POST":
        currentUser=request.session['customer']

        qty=request.POST['qty']
# quantity must be checked later
        varient=request.POST['varient_id']
        product=Product_Varients.objects.get(id=varient)
        check_cart=Cart.objects.filter(customer=currentUser,product=varient).exists()
        
        if check_cart== True:
            message="Product is already in cart"
            return JsonResponse({'message':message})
        else:

            cart=Cart(customer_id=currentUser,product_id=varient,quantity=qty,selling_price=product.Selling_Prize,display_price=product.Display_Prize)
            cart.save()
            count=Cart.objects.filter(customer_id=currentUser).count()
            return JsonResponse({'count':count})

def fnviewcart(request):
    currentUser=request.session['customer']
    user_cart=Cart.objects.filter(customer_id=currentUser)
    cart_count=Cart.objects.filter(customer=currentUser).count()
    wish_count=Wishlist.objects.filter(customer=currentUser).count()
    total_price=0
    total_qty=0
    for items in user_cart:
        total_qty += items.quantity
        total_price += items.selling_price * items.quantity
    
    # cart_total=Cart_total.objects.get(customer_id=currentUser)
    

    # all contexts
    context['cart']=user_cart
    context['total_price']=total_price
    context['total_qty']=total_qty
    context['cart_count']=cart_count
    context['wish_count']=wish_count
    # end contexts

    return render(request,'user_cart.html',context)

def fnremovecartitem(request,cart_item_id):
    print(cart_item_id)
    cart_item=Cart.objects.get(product=cart_item_id)
    print(cart_item)

    if cart_item:
        new_cart=cart_item.delete()
        return redirect(fnviewcart)
    
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

def fnproductlist(request):
    cat_id=request.GET.get('cat_id')
    if cat_id == '0':

        # filter
        orderby="id"
        new=request.GET.get('sort')
       
        # end filter

        products=Product.objects.filter(status="Active")

        paginator=Paginator(products,7)
        page_num=request.GET.get('page')
        newproducts=paginator.get_page(page_num)

        catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
        allcatogory=Catogory.objects.filter(status="Active")
        banners=Banners.objects.all()

        cart_count=0
        wish_count=0

        
        if new=="0":
            orderby="product_varients__id"
            context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
            return render(request,'product_list.html',context)

        if new=="1":
            orderby="product_varients__Selling_Prize"
            context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
            return render(request,'product_list.html',context)
        if new=="2":
            orderby="-product_varients__Selling_Prize"
            context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
            return render(request,'product_list.html',context)


        if 'customer' in request.session:
            currentUser=request.session['customer']
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()
            print(new)
            if new=="0":
               
                orderby="-product_varients__id"
                context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
                return render(request,'product_list.html',context)

            if new == "1":
                print('hai')
                orderby="product_varients__Selling_Prize"
                context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
                return render(request,'product_list.html',context)
            if new=="2":
                orderby="-product_varients__Selling_Prize"
                context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
                return render(request,'product_list.html',context)

            
            context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'currentUser':currentUser,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
            return render(request,'product_list.html',context)

        
        context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count,'cat_id':cat_id,'orderby':orderby}
        return render(request,'product_list.html',context)
    else:
        products=Product.objects.filter(Product_Category=cat_id)

        paginator=Paginator(products,12)
        page_num=request.GET.get('page')
        newproducts=paginator.get_page(page_num)

        catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
        allcatogory=Catogory.objects.filter(status="Active")
        banners=Banners.objects.all()

        cart_count=0
        wish_count=0

        if 'customer' in request.session:
            currentUser=request.session['customer']

            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()

            context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'currentUser':currentUser,'cart_count':cart_count,"wish_count":wish_count}
            return render(request,'product_list.html',context)

        context={'catogory': catogory,'allcat':allcatogory,'products':newproducts,'cart_count':cart_count,"wish_count":wish_count}
        return render(request,'product_list.html',context)




def fnproductitem(request,prod_id):
    product=Product_Varients.objects.get(id=prod_id)
    catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
    allcatogory=Catogory.objects.filter(status="Active")
    cart_count=0
    wish_count=0

    if 'customer' in request.session: 
        currentUser=request.session['customer']
        cart_count=Cart.objects.filter(customer=currentUser).count()
        wish_count=Wishlist.objects.filter(customer=currentUser).count()
        context={'catogory': catogory,'allcat':allcatogory,'product':product,'cart_count':cart_count,"wish_count":wish_count}
        return render(request,'product.html',context)

    context={'catogory': catogory,'allcat':allcatogory,'product':product,'cart_count':cart_count,"wish_count":wish_count}
    return render(request,'product.html',context)

def fnnewproduct(request):
    if request.method=="POST":
        id=request.POST['prod_id']
        varient=request.POST['varient_id']
        product=Product_Varients.objects.get(product=id,Varient_Values_id=varient)
        print(product.Varient_Values)
        data = {
            'Varient_Values':product.Varient_Values.varient_values,
            'id':product.id,
            'Selling_Prize':product.Selling_Prize,
            }
        
        print(data)
        return JsonResponse(data)

def fnchangeqty(request):
    if request.method=="POST":
        currentUser=request.session['customer']
        qty=request.POST.get('qty')
        id=request.POST.get('prod_id')
        print(qty)
        print(id)
        if qty:
            new_cart=Cart.objects.filter(customer_id=currentUser,id=id).update(quantity=qty)
            new_total=Cart.objects.get(customer_id=currentUser,id=id)
            new_item_total=new_total.get_total()

            user_cart=Cart.objects.filter(customer_id=currentUser)
            total_price=0
            total_qty=0
            for items in user_cart:
                total_qty += items.quantity
                total_price += items.selling_price * items.quantity

            data={'new_item_total':new_item_total,'total_qty':total_qty,'total_price':total_price}
        return JsonResponse(data)

def fncheckout(request):
    currentUser=request.session['customer']
    form=AddressForm()
    
    address=Address.objects.filter(username_id=currentUser)
    user_cart=Cart.objects.filter(customer_id=currentUser)
    total_price=0
    total_qty=0
    for items in user_cart:
        total_qty += items.quantity
        total_price += items.selling_price * items.quantity

    context={'cart': user_cart ,'total_price':total_price,'total_qty': total_qty,'address':address,'form':form}

    return render(request,'checkout.html',context)

def fnselectaddress(request):
    if request.method=="POST":
        add_id=request.POST.get('address_id')
        print(add_id)
        currentUser=request.session['customer']
        new_address=Address.objects.get(username_id=currentUser,id=add_id)
        data={'id':new_address.id,'address':new_address.address,'locality':new_address.locality,'district':new_address.district,'state':new_address.state,'country':new_address.country}
        
        return JsonResponse(data)


def fncoupon(request):
    if request.method=="POST":
        coupon=request.POST.get('promo')
        total_price=request.POST.get('price')
        total_pr=float(total_price)
        couponcode=CoupenCode.objects.get(code=coupon)
        coupon_discount=float(couponcode.discount)
        
        validity=couponcode.is_expired
        if validity == True :
            if couponcode.disc_type == "Amount":
                discount=str(couponcode.discount) + 'Rs'
                total=total_price - coupon_discount

            else:
                discount=str(couponcode.discount) + '%'
                total=total_pr -(total_pr * coupon_discount / 100)

            print(total)

            return JsonResponse({'discount':discount,'total_amount':round(total)})

        else:
            message="This coupon code is not valid"

        print(message)
        return JsonResponse({'message':message})

def fnaddress(request):
    currentUser=request.session['customer']
    form=AddressForm()
    context={ 'form':form }
    if request.method=="POST":
        address_type=request.POST['address_type']
        form=AddressForm(request.POST)
        print(form)
        if form.is_valid():
            print('hai')
            address=form.save(commit=False)
            address.username_id=currentUser
            address.address_type=address_type
            if address_type=='home':
                address.default=False
                address.save()
            else:
                address.default=True
                address.save()
            
        else:
            return render(request,'address.html',{'form':form})
            messages.error(request,'form is not valid')
    form=AddressForm()
    context={ 'form':form }
    return render(request,'address.html',context)

def fnaddnewaddress(request):
    currentUser=request.session['customer']
    address=request.POST['add']
    locality=request.POST['locality']
    district=request.POST['district']
    state=request.POST['state']
    country=request.POST['country']
    pin=request.POST['pin']
    landmark=request.POST['landmark']
    address_type=request.POST['address_type']
    new_address=Address(username_id=currentUser,pin=pin,locality=locality,address=address,state=state,district=district,landmark=landmark,country=country,default=0,address_type=address_type).save()
    return redirect(fncheckout)


def fnnew(request):
    return render(request,'news.html')

def fnoffers(request):
    pass
            
        
