from django.db import models
from EcomAdmin.models import Product,Customer,Product_Varients


# Create your models here.
class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    subject=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product_Varients,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    selling_price=models.DecimalField(max_digits=12,decimal_places=2)
    display_price=models.DecimalField(max_digits=12,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def get_total(self):
        total=self.selling_price * self.quantity
        float_total=format(total,'0.2f')
        return float_total

    class Meta:
        db_table = "Cart"
        ordering = ['-created']

class Cart_total(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_total=models.DecimalField(max_digits=12,decimal_places=2)
    total_quantity=models.PositiveIntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    





