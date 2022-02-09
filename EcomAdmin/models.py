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
    bannner_name=models.CharField(max_length=100)
    banner_url=models.URLField(max_length=100)
    banner_image=models.FileField(upload_to='images/Banner')
    app_banner_image=models.FileField(upload_to='images/Banner_app')
    display_order=models.IntegerField()
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Banner'

class Brand(models.Model):
    brand_name=models.CharField(max_length=100)
    brand_image=models.ImageField(upload_to='images/brand')
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))

    class Meta:
        db_table='Brand'

class Catogory(models.Model):
    catogory_name=models.CharField(max_length=100)
    catogory_image=models.FileField(upload_to='images/catogory')
    display_order=models.IntegerField()
    parent=models.ForeignKey('Catogory',on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    class Meta:
        db_table='Catogory'

    def __str__(self):
        return self.catogory_name

class VarientType(models.Model):
    varient_name=models.CharField(max_length=100)
    display_order=models.IntegerField()
    status=models.CharField(max_length=20,default='active',choices=(
        ('active','active'),
        ('inactive','inactive')
    ))

    class Meta:
        db_table='Varient Type'

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
    class Meta:
        db_table='Varient Values'

class Offers(models.Model):
    offer_name=models.CharField(max_length=100)
    offer_image=models.ImageField(upload_to='images/offers')
    offer_app_image=models.ImageField(upload_to='images/offers/app_image')
    status=models.CharField(max_length=30,choices=(
        ('active','active'),
        ('inactive','inactive')
    ))
    class Meta:
        db_table='Offers'

class Area(models.Model):
    pass








