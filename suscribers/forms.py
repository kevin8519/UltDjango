'''
Created on Oct 3, 2016

@author: kevin
'''
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

from models import Subscriber


class AddressMixin(forms.ModelForm):
    address_one = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     
    address_two = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     
    city=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=Subscriber
        fields = ('address_one', 'address_two', 'city', 'state',)
        
         




class SuscriberForm(AddressMixin,UserCreationForm):
    
            
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
     
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    username = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
    
    password1 = forms.CharField(required=True,
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
        )
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'password'})
        
        
        
        
        ) 
    
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data["email"]
        user.username=self.cleaned_data["username"]
        user.password=self.cleaned_data["password1"]
        
        if commit:
            user.save()
        return user    

    
                         