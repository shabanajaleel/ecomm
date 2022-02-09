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
        widgets={
            'banner_name' : forms.TextInput(attrs={'class':'form-control'}),
            'banner_url' : forms.URLInput(attrs={'class':'form-control'}),
            'banner_image' : forms.FileInput(attrs={'class':'form-control'}),
            'app_banner_image' : forms.FileInput(attrs={'class':'form-control'}),
            'display_order' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.Select(attrs={'class':'form-control'})
        }

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









            
        