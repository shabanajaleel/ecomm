from django.shortcuts import render
from random import randint
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from EcomAdmin.models import *
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

        data={'wish_count':0,'cart_count':0,'banners':banner_serializer.data,'category_list':catogory_serializer.data}
        return JsonResponse(data, status=201)


    if request.method=="POST":
        data=JSONParser().parse(request)
        pass


    









