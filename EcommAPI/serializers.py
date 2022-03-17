from rest_framework import serializers
from EcomAdmin.models import Customer
from django.contrib.auth.hashers import make_password

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        customer=Customer(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            phone=self.validated_data['phone'],
            password = make_password(self.validated_data['password'])

        )
        customer.save()
        
       