from django.shortcuts import render
from random import randint
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from EcomAdmin.models import *
from EcomUser.models import *
from django.db.models import Sum,Count
from django.contrib.auth.hashers import make_password,check_password
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Create your views here.
@csrf_exempt
def fnapi_register(request):

    # if request.method=='GET':
    #     customer=Customer.objects.all()
    #     obj1=CustomerSerializer(customer,many='True') 
    #     return JsonResponse(obj1.data,safe=False)


    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data={'response_code':0,'message':"Successfully Registered"}
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def fnapi_login(request):

    if request.method=='POST':
        data = JSONParser().parse(request)
        phone=data.get('phone')
        password=data.get('password')
        print(phone)

        try:
            customer=Customer.objects.get(phone=phone)
            enc_password=check_password(password,customer.password)
            if enc_password == True:
                if customer.session_id:
                    data={'response_code':0,'message':"Logged In Successfully",'session_id':customer.session_id,'name':customer.name,'phone':customer.phone,'uid':customer.id}
                    return JsonResponse(data, status=201)
                else:
                    session_id=str(randint(1000000000,9999999999))
                    print(session_id)
                    customer.session_id=session_id
                    customer.save()
                    data={'response_code':0,'message':"Logged In Successfully",'session_id':customer.session_id,'name':customer.name,'phone':customer.phone,'uid':customer.id}
                    return JsonResponse(data, status=201)
                    
            data={'response_code':1,'message':"Invalid Password"}
            return JsonResponse(data, status=201)

        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid Phone Number"}
            return JsonResponse(data, status=201)

@csrf_exempt
def verify_otp(request):
    if request.method=='POST':
        data=JSONParser().parse(request)
        otp=data.get('otp')
        phone=data.get('phone')
        user_id=data.get('user_id')
        try:
            customer=Customer.objects.get(id=user_id,phone=phone)
            if customer.otp == otp:
                data={'response_code':0,'message':"OTP Verified"}
                return JsonResponse(data, status=201)
            else:
                data={'response_code':1,'message':"Incorrect OTP"}
                return JsonResponse(data, status=201)
            

        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Incorrect User Details"}
            return JsonResponse(data, status=201)

@csrf_exempt
def resend_otp(request):
    data=JSONParser().parse(request)
    phone=data.get('phone')
    otp=str(randint(1000,9999))    
    message = client.messages \
            .create(
                body="Your OTP for login is" + otp,
                from_='+19107765960',
                to='+91' + str(phone)
            )
    if message:
        data={'response_code':0,'message':"OTP Resend Successfully"}
        return JsonResponse(data, status=201)
    else:
        data={'response_code':1,'message':"Unable to Send OTP"}
        return JsonResponse(data, status=201)

@csrf_exempt
def fnhomeapi(request):
    if request.method=='GET':

        # get Banner
        banners=Banners.objects.filter(status="Active")
        banner_serializer=BannerSerializer(banners,many='True')

        #get catogory
        catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
        catogory_serializer=CatogorySerializer(catogory,many='True')

        # get latest product
        products=Product.objects.filter(status="Active")
        latest_product_serializer=LatestProductSerializer(products,many=True)


        data={'wish_count':0,'cart_count':0,'banners':banner_serializer.data,'category_list':catogory_serializer.data,"latest_product":latest_product_serializer.data,"response_code":0,'message':"success"}
        return JsonResponse(data, status=201)


    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        try:

            # get User
            customer=Customer.objects.get(session_id=s_id)
            print(customer.id)
            currentUser=customer.id

            # get Banner
            banners=Banners.objects.filter(status="Active")
            banner_serializer=BannerSerializer(banners,many='True')

            #get catogory
            catogory=Catogory.objects.filter(parent=None ,status="Active").order_by('display_order')
            catogory_serializer=CatogorySerializer(catogory,many='True')

            # get latest product
            products=Product.objects.filter(status="Active")
            latest_product_serializer=LatestProductSerializer(products,many=True)

            # wish-count and cart-count
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()

            data={'wish_count':wish_count,'cart_count':cart_count,'banners':banner_serializer.data,'category_list':catogory_serializer.data,"latest_product":latest_product_serializer.data,"response_code":0,'message':"success"}
            return JsonResponse(data, status=201)


        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid User"}
            return JsonResponse(data)

@csrf_exempt
def fnallproducts(request):
    if request.method=="GET":
        products=Product.objects.filter(status="Active")
        productserializer=ProductSerializer(products,many="True")

        data={'wish_count':0,'cart_count':0,"All Products":productserializer.data,"response_code":0,'message':"success"}
        return JsonResponse(data, status=201)

    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        cat_id=data.get('cat_id')

        if s_id:
            if cat_id is None:
                products=Product.objects.filter(status="Active")
                productserializer=ProductSerializer(products,many="True")

                customer=Customer.objects.get(session_id=s_id)
                currentUser=customer.id

                cart_count=Cart.objects.filter(customer=currentUser).count()
                wish_count=Wishlist.objects.filter(customer=currentUser).count()

                data={'wish_count':wish_count,'cart_count':cart_count,"All Products":productserializer.data,"response_code":0,'message':"success"}
                return JsonResponse(data, status=201)
            
            if cat_id:

                products=Product.objects.filter(Product_Category=cat_id,status="Active")
                productserializer=ProductSerializer(products,many="True")

                customer=Customer.objects.get(session_id=s_id)
                currentUser=customer.id

                cart_count=Cart.objects.filter(customer=currentUser).count()
                wish_count=Wishlist.objects.filter(customer=currentUser).count()

                data={'wish_count':wish_count,'cart_count':cart_count,"All Products":productserializer.data,"response_code":0,'message':"success"}
                return JsonResponse(data, status=201)

        elif cat_id:
            products=Product.objects.filter(Product_Category=cat_id,status="Active")
            productserializer=ProductSerializer(products,many="True")

            data={'wish_count':0,'cart_count':0,"All Products":productserializer.data,"response_code":0,'message':"success"}
            return JsonResponse(data, status=201)

@csrf_exempt
def fnproductdetails(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        product_varient_id=data.get('varient_id')

        products=Product_Varients.objects.filter(id=product_varient_id)
        print(products.product.id)
        image=ProductImage.objects.filter(product_id=products.product.id)
        print(image)
        image_serializer=ProductImageSerializer(image,many="True")

        # productvarientserializer=ProductVarientSerializer(products,many="False")

        data={'wish_count':0,'cart_count':0,"Product":productvarientserializer.data,"images":image_serializer.data,"response_code":0,'message':"success"}
        return JsonResponse(data, status=201)



@csrf_exempt
def fnaddtocart(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        varient_id=data.get('varient_id')
        qty=data.get('qty')

        try:
            # get user
            customer=Customer.objects.get(session_id=s_id)
            currentUser=customer.id


            # check product quantity
            product=Product_Varients.objects.get(id=varient_id)
            if product.Product_stock < int(qty):
                data={'response_code':1,'message':"Product is out of stock"}
                return JsonResponse(data)

            else:
                # check if product already exists in cart
                check_cart=Cart.objects.filter(customer=currentUser,product=varient_id).exists()
                
                if check_cart== True:
                    data={'response_code':1,'message':"Product is already in cart"}
                    return JsonResponse(data)

                else:

                    cart=Cart(customer_id=currentUser,product_id=varient_id,quantity=qty,selling_price=product.Selling_Prize,display_price=product.Display_Prize)
                    cart.save()

                    # wish-count and cart-count
                    cart_count=Cart.objects.filter(customer=currentUser).count()
                    wish_count=Wishlist.objects.filter(customer=currentUser).count()

                    data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Product added to cart successfully"}
                    return JsonResponse(data)

        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid User"}
            return JsonResponse(data)    

@csrf_exempt
def fnaddtowishlist(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        varient_id=data.get('varient_id')

        try:
            # get user
            customer=Customer.objects.get(session_id=s_id)
            currentUser=customer.id

            product=Product_Varients.objects.get(id=varient_id)
            check_wishlist=Wishlist.objects.filter(customer=currentUser,product=varient_id).exists()
            
            if check_wishlist== True:
                data={'response_code':1,'message':"Product is already in Wishlist"}
                return JsonResponse(data)

            else:

                wishlist=Wishlist(customer_id=currentUser,product_id=varient_id,unit_price=product.Selling_Prize)
                wishlist.save()


                cart_count=Cart.objects.filter(customer=currentUser).count()
                wish_count=Wishlist.objects.filter(customer=currentUser).count()

                data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Product added to Wishlist successfully"}
                return JsonResponse(data)


        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid User"}
            return JsonResponse(data)

@csrf_exempt
def fnviewcart(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        try:
            # get user
            customer=Customer.objects.get(session_id=s_id)
            currentUser=customer.id

            # get cart item
            cart=Cart.objects.filter(customer=currentUser)
            cartserializer=ViewCartSerializer(cart,many=True)

            # cart total
            cart_total=0
            for items in cart:
                cart_total += items.selling_price * items.quantity

                # if items.quantity < items.product.Product_stock:
                #     stock_status=1
                # elif items.quantity > items.product.Product_stock:
                #     stock_status=0
                # else items.product.Product_stock == 0:
                #     stock_status=2


            # get cart-wish count
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()


            data={'wish_count':wish_count,'cart_count':cart_count,'cart_total':cart_total,'products':cartserializer.data,'response_code':0,'message':"success"}
            return JsonResponse(data)


        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid User"}
            return JsonResponse(data)

@csrf_exempt
def fnupdatecart(request):
    if request.method=='PUT':
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        id=data.get('cart_id')
        customer=Customer.objects.get(session_id=s_id)
        currentUser=customer.id

        cart=Cart.objects.get(customer=currentUser,id=id)

        cartserializer=CartSerializer(cart,data)
        if cartserializer.is_valid():
            cartserializer.save()

            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()


            data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Cart Updated Successfully"}
            return JsonResponse(data)
        else:
            return JsonResponse(cartserializer.errors)

@csrf_exempt
def fnremovecart(request):
    if request.method=='DELETE':
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        cart_id=data.get('cart_id')

        customer=Customer.objects.get(session_id=s_id)
        currentUser=customer.id

        

        try:
            cart=Cart.objects.get(id=cart_id,customer_id=currentUser)
            cart.delete()

            #cart and wish count 
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()


            data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Cart removed Successfully"}
            return JsonResponse(data)

        except Cart.DoesNotExist:
            data={'response_code':1,'message':"Invalid Entries"}
            return JsonResponse(data)

@csrf_exempt
def fnviewwishlist(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        try:
            # get user
            customer=Customer.objects.get(session_id=s_id)
            currentUser=customer.id

            # get cart item
            wishlist=Wishlist.objects.filter(customer=currentUser)
            wishserializer=ViewWishlistSerializer(wishlist,many=True)

            # get cart-wish count
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()


            data={'wish_count':wish_count,'cart_count':cart_count,'products':wishserializer.data,'response_code':0,'message':"success"}
            return JsonResponse(data)


        except Customer.DoesNotExist:
            data={'response_code':1,'message':"Invalid User"}
            return JsonResponse(data)

@csrf_exempt
def fnremovewishlist(request):
    if request.method=='DELETE':
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        wish_id=data.get('wish_id')

        customer=Customer.objects.get(session_id=s_id)
        currentUser=customer.id

        

        try:
            wish=Wishlist.objects.get(id=wish_id,customer_id=currentUser)
            wish.delete()

            #cart and wish count 
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()


            data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Item removed from wishlist"}
            return JsonResponse(data)

        except Wishlist.DoesNotExist:
            data={'response_code':1,'message':"Invalid Entries"}
            return JsonResponse(data)

@csrf_exempt
def fnwishtocart(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        s_id=data.get('s_id')
        wish_id=data.get('wish_id')
        product_varient_id=data.get('varient_id')
        qty=data.get('qty')

        print("hai")
        product=Product_Varients.objects.get(id=product_varient_id)
        print(product)

        customer=Customer.objects.get(session_id=s_id)
        currentUser=customer.id
        print(currentUser)
        check_cart=Cart.objects.filter(customer=currentUser,product=product_varient_id).exists()
        print(check_cart)

        if check_cart== True:
            data={'response_code':1,'message':"Item Already exist in cart"}
            return JsonResponse(data)
        else:

            cart=Cart(customer_id=currentUser,product_id=product_varient_id,quantity=qty,selling_price=product.Selling_Prize,display_price=product.Display_Prize)
            cart.save()
            wishlist=Wishlist.objects.filter(customer_id=currentUser,product_id=product_varient_id)
            wishlist.delete()

            #cart and wish count 
            cart_count=Cart.objects.filter(customer=currentUser).count()
            wish_count=Wishlist.objects.filter(customer=currentUser).count()

            data={'wish_count':wish_count,'cart_count':cart_count,'response_code':0,'message':"Item added to cart succesfully"}
            return JsonResponse(data)











        




            




    






            



    









