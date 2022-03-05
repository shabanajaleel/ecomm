from tkinter import Widget
from django import forms
from . models import *
from django.core.files.images import get_image_dimensions
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import get_user_model
import re

User=get_user_model()

PHONE_REGEX="^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$"


class DateInput(forms.DateInput):
    input_type = 'date'


class AdminRoleForm(forms.ModelForm):
    class Meta:
        model=AdminRole
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(AdminRoleForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class CustomUserForm(UserCreationForm):
    class Meta:
        model=CustomAdmin
        fields=('username','password1','password2','email','role','phone')
    
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def save(self,commit=True):
        user=super(CustomUserForm,self).save(commit=False)
        user.role=self.cleaned_data['role']
        user.phone=self.cleaned_data['phone']
        if commit:
            user.save()
            return user

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'Username already exist.')

class EditUserForm(UserChangeForm):
    class Meta:
        model=CustomAdmin
        fields=('username','email','role','phone')
    
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def save(self,commit=True):
        user=super(EditUserForm,self).save(commit=False)
        user.role=self.cleaned_data['role']
        user.phone=self.cleaned_data['phone']
        if commit:
            user.save()
            return user

    # def clean_username(self, username):
    #     user_model = get_user_model() # your way of getting the User
    #     try:
    #         user_model.objects.get(username__iexact=username)
    #     except user_model.DoesNotExist:
    #         return username
    #     raise forms.ValidationError(_("This username has already existed."))

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
    
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def save(self,commit=True):
        user=super(ChangePasswordForm,self).save(commit=False)
        user.set_password(self.cleaned_data["new_password1"])
        if commit:
            user.save()
            return user

# class ChangePasswordForm(PasswordChangeForm):
#     class Meta:
#         model=CustomAdmin
#         fields=('')
    
#     def __init__(self, *args, **kwargs):
#         super(ChangePasswordForm, self).__init__(*args, **kwargs)
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({'class':'form-control'})

#     def save(self,commit=True):
#         user=super(ChangePasswordForm,self).save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#             return user


class MainPathForm(forms.ModelForm):
    class Meta:
        model=Path
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(MainPathForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})




class BannerForm(forms.ModelForm):

    class Meta:
        model=Banners
        fields="__all__"
    

    # def clean_banner_image(self):
    #    banner_image = self.cleaned_data.get("banner_image")
    #    if not banner_image:
    #        raise forms.ValidationError("No image!")
    #    else:
    #        w, h = get_image_dimensions(banner_image)
    #        if w > 235:
    #            raise forms.ValidationError("The Banner image is %i pixel wide. It's supposed to be 235px" % w)
    #        if h > 145:
    #            raise forms.ValidationError("The Banner Imageis %i pixel high. It's supposed to be 145px" % h)
    #    return banner_image

    # def clean_banner_app_image(self):
    #     banner_app_image = self.cleaned_data.get("banner_app_image")
    #     if not banner_app_image:
    #         raise forms.ValidationError("No image!")
    #     else:
    #         w, h = get_image_dimensions(banner_app_image)
    #         if w > 900:
    #             raise forms.ValidationError("The Banner App image is %i pixel wide. It's supposed to be 900px" % w)
    #         if h > 450:
    #             raise forms.ValidationError("The Banner App Imageis %i pixel high. It's supposed to be 450px" % h)
    #     return banner_app_image

    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields="__all__"

    def clean_brand_image(self):
       brand_image = self.cleaned_data.get("brand_image")
       if not brand_image:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(brand_image)
           if w > 128:
               raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 128px" % w)
           if h > 128:
               raise forms.ValidationError("The image is %i pixel high. It's supposed to be 128px" % h)
       return brand_image


    def __init__(self, *args, **kwargs):
        super(BrandForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class CatogoryForm(forms.ModelForm):
    class Meta:
        model=Catogory
        fields="__all__"

    # def clean_catogory_image(self):
    #     catogory_image = self.cleaned_data.get("catogory_image")
    #     if not catogory_image:
    #         raise forms.ValidationError("No image!")
    #     else:
    #         w, h = get_image_dimensions(catogory_image)
    #         if w > 1200 or w < 1200:
    #             raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 1200px" % w)
    #         if h > 600 or h < 600:
    #             raise forms.ValidationError("The image is %i pixel high. It's supposed to be 600px" % h)
    #     return catogory_image
       


    def __init__(self, *args, **kwargs):
        super(CatogoryForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class VarientTypeForm(forms.ModelForm):
    class Meta:
        model=VarientType
        fields="__all__"


    def __init__(self, *args, **kwargs):
        super(VarientTypeForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})


class VarientValuesForm(forms.ModelForm):
    class Meta:
        model=VarientValues
        fields="__all__"


    def __init__(self, *args, **kwargs):
        super(VarientValuesForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})


class OffersForm(forms.ModelForm):
    class Meta:
        model=Offers
        fields="__all__"


    def __init__(self,*args , **kwargs):
        super(OffersForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    def clean_offer_image(self):
       offer_image = self.cleaned_data.get("offer_image")
       if not offer_image:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(offer_image)
           if w > 235:
               raise forms.ValidationError("The offer image is %i pixel wide. It's supposed to be 235px" % w)
           if h > 145:
               raise forms.ValidationError("The offer Imageis %i pixel high. It's supposed to be 145px" % h)
       return offer_image

    def clean_offer_app_image(self):
       offer_app_image = self.cleaned_data.get("offer_app_image")
       if not offer_app_image:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(offer_app_image)
           if w > 900:
               raise forms.ValidationError("The offer App image is %i pixel wide. It's supposed to be 900px" % w)
           if h > 450:
               raise forms.ValidationError("The offer App Imageis %i pixel high. It's supposed to be 450px" % h)
       return offer_app_image

class AreaForm(forms.ModelForm):
    class Meta:
        model=Area
        fields="__all__"


    def __init__(self,*args , **kwargs):
        super(AreaForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class PincodeForm(forms.ModelForm):
    class Meta:
        model=Pincode
        fields="__all__"


    def __init__(self,*args , **kwargs):
        super(PincodeForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        exclude=['profile_image','status','otp']


    def __init__(self,*args , **kwargs):
        super(CustomerForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Mobile No'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['conf_password'].widget.attrs['placeholder'] = 'Confirm Password'
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})
            self.fields[name].label = ""

    def clean_conf_password(self):
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("conf_password")
        if password and conf_password and password != conf_password:
            raise forms.ValidationError("Passwords do not match")
        return conf_password

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not re.match(PHONE_REGEX,str(phone))  :
            raise forms.ValidationError('Invalid phone Number')
        return phone


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"

    def __init__(self,*args , **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

class ProductVarientForm(forms.ModelForm):
    class Meta:
        model=Product_Varients
        fields="__all__"

    def __init__(self,*args , **kwargs):
        super(ProductVarientForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})

    # def clean_Selling_Prize(self):
    #     Selling_Prize=self.cleaned_data.get("Selling_Prize")
    #     Display_Prize=self.cleaned_data.get("Display_Prize")
    #     if Selling_Prize > Display_Prize:
    #         raise forms.ValidationError("Selling price greater than display price")
    #     return Selling_Prize
    
class CouponCodeForm(forms.ModelForm):
    class Meta:
        model=CoupenCode
        fields="__all__"
        widgets={
            'startdate':DateInput(),
            'enddate':DateInput(),
        }

    def __init__(self,*args , **kwargs):
        super(CouponCodeForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})




            
        