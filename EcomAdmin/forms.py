from tkinter import Widget
from django import forms
from . models import *
from django.core.files.images import get_image_dimensions

class AdminRoleForm(forms.ModelForm):
    class Meta:
        model=AdminRole
        fields="__all__"
        widgets={
            'role_name' : forms.TextInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'})
        }




class BannerForm(forms.ModelForm):

    class Meta:
        model=Banners
        fields="__all__"
    

    def clean_banner_image(self):
       banner_image = self.cleaned_data.get("banner_image")
       if not banner_image:
           raise forms.ValidationError("No image!")
       else:
           w, h = get_image_dimensions(banner_image)
           if w > 235:
               raise forms.ValidationError("The Banner image is %i pixel wide. It's supposed to be 235px" % w)
           if h > 145:
               raise forms.ValidationError("The Banner Imageis %i pixel high. It's supposed to be 145px" % h)
       return banner_image

    def clean_banner_app_image(self):
        banner_app_image = self.cleaned_data.get("banner_app_image")
        if not banner_app_image:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(banner_app_image)
            if w > 900:
                raise forms.ValidationError("The Banner App image is %i pixel wide. It's supposed to be 900px" % w)
            if h > 450:
                raise forms.ValidationError("The Banner App Imageis %i pixel high. It's supposed to be 450px" % h)
        return banner_app_image

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

    def clean_catogory_image(self):
        catogory_image = self.cleaned_data.get("catogory_image")
        if not catogory_image:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(catogory_image)
            if w > 1200:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 1200px" % w)
            if h > 600:
                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 600px" % h)
        return catogory_image
       


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


    def __init__(self,*args , **kwargs):
        super(CustomerForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})



            
        