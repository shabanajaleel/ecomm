from rest_framework import serializers
from EcomAdmin.models import Customer,Banners,Catogory
from django.contrib.auth.hashers import make_password
from random import randint
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):

        otp=str(randint(1000,9999))
        phone=self.validated_data['phone'],
        
        message = client.messages \
                .create(
                    body="Your OTP for login is" + otp,
                    from_='+19107765960',
                    to='+91' + str(phone)
                )
       

        customer=Customer(
            
            name=self.validated_data['name'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],
            password = make_password(self.validated_data['password']),
            otp=otp

        )
       
        customer.save()

class LoginSerializer(serializers.ModelSerializer):
    response_code = serializers.SerializerMethodField() # add field
    message = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ['name', 'session_id','id','phone','response_code','message']

    def get_response_code(self):
        return 0

    def get_message(self):
        message="Logged in Successfully"
        return message


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields =['id','banner_name', 'banner_url','app_banner_image']

class CatogorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catogory
        fields = ['id','catogory_name','catogory_image']


class ProductSerializer(serializers.ModelSerializer):
    pass




       
    

        
       