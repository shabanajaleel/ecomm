from django import forms
from . models import *
from EcomAdmin .models import Address
from django.core.exceptions import ValidationError
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_REGEX="^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$"

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email and not re.match(EMAIL_REGEX, str(email)):
            raise forms.ValidationError('Invalid email format')

        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if phone and not re.match(PHONE_REGEX,str(phone))  :
            raise forms.ValidationError('Invalid phone Number')

        return phone

    # def clean(self):
    #   super(FeedbackForm, self).clean()

    #   # getting username and password from cleaned_data
    #   name = self.cleaned_data.get('name')
    #   email = self.cleaned_data.get('email')
    #   phone = self.cleaned_data.get('phone')
    #   description = self.cleaned_data.get('description')

    #   # validating the username and password
    #   if name == "":
    #      self._errors['name'] = self.error_class(['Name is required'])

    # #   if len(password) < 8:
    # #      self._errors['password'] = self.error_class(['Password length should not be less than 8 characters'])

    #   return self.cleaned_data

class AddressForm(forms.ModelForm):

    class Meta:
        model=Address
        fields="__all__"
        exclude=['default']

    def __init__(self,*args , **kwargs):
        super(AddressForm,self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({'class':'form-control'})