from rest_framework import serializers
from EcomAdmin.models import Customer,Banners,Catogory,Product_Varients,Product,ProductImage
from EcomUser.models import Cart,Wishlist
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


class LatestProductSerializer(serializers.ModelSerializer):
    Sku_Code=serializers.CharField(source='product_varients_set.first.Sku_Code')
    Selling_Prize=serializers.CharField(source='product_varients_set.first.Selling_Prize')
    Cut_Prize=serializers.CharField(source='product_varients_set.first.Display_Prize')
    prod_varient_id=serializers.CharField(source='product_varients_set.first.id')
    prod_image=serializers.CharField(source='productimage_set.first.Thumbnail_image')
    


    class Meta:
        model = Product
        fields=['id','prod_varient_id','Name','Sku_Code','prod_image','Selling_Prize','Cut_Prize']
   
class ViewCartSerializer(serializers.ModelSerializer):

    user_id=serializers.CharField(source="customer.id")
    product_code=serializers.CharField(source="product.Sku_Code")
    product_varient_id=serializers.CharField(source="product.id")
    product_name=serializers.CharField(source="product.product.Name")
    product_image=serializers.CharField(source="product.product.productimage_set.first.Thumbnail_image")
    productvarient_values=serializers.CharField(source="product.Varient_Values.varient_values")
    class Meta:
        model = Cart
        fields = ['id','user_id','product_code','product_varient_id','product_name','product_image','productvarient_values','quantity','selling_price','display_price','get_total']

class CartSerializer(serializers.ModelSerializer):
     class Meta:
        model = Cart
        fields = ['id','quantity']

class ViewWishlistSerializer(serializers.ModelSerializer):

    user_id=serializers.CharField(source="customer.id")
    product_code=serializers.CharField(source="product.Sku_Code")
    product_id=serializers.CharField(source="product.product.id")
    product_varient_id=serializers.CharField(source="product.id")
    product_name=serializers.CharField(source="product.product.Name")
    product_image=serializers.CharField(source="product.product.productimage_set.first.Thumbnail_image")
    productvarient_values=serializers.CharField(source="product.Varient_Values.varient_values")
    
    class Meta:
        model = Wishlist
        fields = ['id','user_id','product_code', 'product_id','product_varient_id','product_name','product_image','productvarient_values','unit_price']

class ProductSerializer(serializers.ModelSerializer):
    Sku_Code=serializers.CharField(source='product_varients_set.first.Sku_Code')
    Selling_Prize=serializers.CharField(source='product_varients_set.first.Selling_Prize')
    Cut_Prize=serializers.CharField(source='product_varients_set.first.Display_Prize')
    prod_varient_id=serializers.CharField(source='product_varients_set.first.id')
    prod_image=serializers.CharField(source='productimage_set.first.Thumbnail_image')
    
    class Meta:
        model = Product
        fields=['id','prod_varient_id','Name','Sku_Code','prod_image','Selling_Prize','Cut_Prize']

class ProductVarientSerializer(serializers.ModelSerializer):
    product_id=serializers.CharField(source='product.id')
    product_name=serializers.CharField(source='product.Name')
    product_description=serializers.CharField(source='product.Description')
    class Meta:
        model=Product_Varients
        fields=['id','Sku_Code','Display_Prize','Selling_Prize','product_id','product_name','product_description']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fileds=['id','Thumbnail_image']

       
    

        
       