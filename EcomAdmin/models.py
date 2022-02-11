import os
from django.db import models

# Create your models here.
class AdminRole(models.Model):
    role_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=(
        ('active','active'),
        ('inactive','inactive')
    ))

    def __str__(self):
        return self.role_name

class Banners(models.Model):
    banner_name=models.CharField(max_length=100)
    banner_url=models.URLField(max_length=100)
    banner_image=models.FileField(upload_to='images/Banner')
    app_banner_image=models.FileField(upload_to='images/Banner_app')
    is_intermediate=models.BooleanField(default=True)
    display_order=models.IntegerField()
    status=models.CharField(max_length=20,default='active',choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Banner'
        ordering = ['-Created_at']

class Brand(models.Model):
    brand_name=models.CharField(max_length=100)
    brand_image=models.ImageField(upload_to='images/brand')
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)

    # def filename(self):
    #     return os.path.basename(self.brand_image.name)

    class Meta:
        db_table='Brand'
        ordering = ['-Created_at']

class Catogory(models.Model):
    catogory_name=models.CharField(max_length=100)
    catogory_image=models.ImageField(upload_to='images/catogory')
    display_order=models.IntegerField()
    parent=models.ForeignKey('Catogory',on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Catogory'
        ordering = ['-Created_at']

    def __str__(self):
        return self.catogory_name

class VarientType(models.Model):
    varient_name=models.CharField(max_length=100)
    display_order=models.IntegerField()
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Varient Type'
        ordering = ['-Created_at']

    def __str__(self):
        return self.varient_name

class VarientValues(models.Model):
    varient_values=models.CharField(max_length=100)
    varient_type=models.ForeignKey(VarientType,on_delete=models.CASCADE)
    display_order=models.IntegerField()
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Varient Values'
        ordering = ['-Created_at']

class Offers(models.Model):
    offer_name=models.CharField(max_length=100)
    offer_image=models.ImageField(upload_to='images/offers')
    offer_app_image=models.ImageField(upload_to='images/offers/app_image')
    status=models.CharField(max_length=30,choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Offers'
        ordering = ['-Created_at']

class Area(models.Model):
    area_name=models.CharField(max_length=100)
    status=models.CharField(max_length=30,choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='Area'
        ordering = ['-Created_at']

    def __str__(self):
        return self.area_name

class Pincode(models.Model):
    pincode=models.CharField(max_length=10)
    postoffice=models.CharField(max_length=100)
    area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True,blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=30,choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    class Meta:
        db_table='Pincode'
        ordering = ['-Created_at']
        

    def __str__(self):
        return self.area_name


class Customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    profile_image=models.ImageField(upload_to='images/profile',null=True,blank=True)
    registered_date=models.DateTimeField(auto_now_add=True)
    password=models.CharField(max_length=20)
    conf_password=models.CharField(max_length=20)
    status=models.BooleanField(default=True)

    class Meta:
        db_table='Customer'
        ordering = ['-registered_date']
        

    def __str__(self):
        return self.username










