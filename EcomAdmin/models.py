import os
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MainPath(models.Model):
    path_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Main Path'
        ordering = ['-Created_at']

    def __str__(self):
        return self.path_name

class SubPath(models.Model):
    main_path=models.ForeignKey(MainPath,on_delete=models.CASCADE)
    path_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    display_order=models.IntegerField()
    Created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'Sub Path'
        ordering = ['-Created_at']

    def __str__(self):
        return self.path_name

class AdminRole(models.Model):
    role_name=models.CharField(max_length=100)
    status=models.CharField(max_length=20,choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    permissions=models.ManyToManyField(SubPath,null=True,blank=True)
    Created_at = models.DateTimeField(auto_now=True)

    
    class Meta:
        db_table = 'AdminRole'
        ordering = ['-Created_at']


    def __str__(self):
        return self.role_name

class CustomAdmin(AbstractUser):
    role=models.ForeignKey(AdminRole,on_delete=models.CASCADE,null=True,blank=True)
    phone=models.BigIntegerField(null=True)
    status=models.CharField(max_length=20,default="Active",choices=(
        ('Active','Active'),
        ('Inactive','Inactive')
    ))
    Created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CustomAdmin'
        ordering = ['-Created_at']



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

class Product_Varients(models.Model):
    Varient_name = models.CharField(max_length=255)
    Varient_Values = models.ForeignKey(VarientValues,on_delete=models.CASCADE)
    Product_Offers = models.ManyToManyField(Offers,blank=True)
    Selling_Prize = models.DecimalField(max_digits=12,decimal_places=2)
    Display_Prize = models.DecimalField(max_digits=12,decimal_places=2)
    Product_stock = models.PositiveIntegerField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Active',max_length=20, choices=(
        ('Active','Active'),
        ('Pending','Pending'),
        ('Suspended','Suspended'),
    ))
    class Meta:
        db_table = "Product_Varients"

class Product(models.Model):
    Name = models.CharField(max_length=250)
    Description = models.TextField()
    Thumbnail_image = models.FileField(upload_to='Products',null=True)
    Varient_Type = models.ForeignKey(VarientType,on_delete=models.CASCADE)
    Product_Category = models.ForeignKey(Catogory,on_delete=models.CASCADE)
    Product_Brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True,null=True)
    Product_Items = models.ManyToManyField(Product_Varients,verbose_name='ProductItems',blank=True)
    status = models.CharField(default='Active',max_length=20, choices=(
        ('Active','Active'),
        ('Pending','Pending'),
        ('Suspended','Suspended'),
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Products"
    def __str__(self) -> str:
        return self.Name


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

class Address(models.Model):
    username = models.ForeignKey(Customer,on_delete=models.CASCADE)
    pin = models.ForeignKey(Pincode,on_delete=models.CASCADE)
    locality = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    state = models.CharField(max_length=20,choices=(('kerala','kerala'),))
    district = models.CharField(max_length=20,choices=(('kozhikode','kozhikode'),))
    landmark = models.TextField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=20,choices=(('india','india'),))
    default = models.BooleanField(default=False)
    address_type = models.CharField(max_length=20,choices=(('home','home'),('work','work'),))

    class Meta:
        db_table = 'address'

class OrderDetails(models.Model):
    orderid=models.CharField(max_length=100)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=20,choices=(
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Shipped','Shipped'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),),default='Pending')
    order_total = models.DecimalField(max_digits=20,decimal_places=2)
    totalcount=models.CharField(max_length=50)
    payment_mode= models.CharField(max_length=20,choices=(
        ('COD','COD'),
        ('PAYMENT','PAYMENT')))

    payment_status = models.CharField(max_length=20,choices=(
        ('Pending','Pending'),
        ('Received','Received')))
    platform=models.CharField(max_length=100)

class Order(models.Model):
    order_id=models.ForeignKey(OrderDetails,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    count=models.CharField(max_length=50)
    order_total = models.DecimalField(max_digits=20,decimal_places=2)
    order_date=models.DateField(auto_now_add=True)
    
        




















