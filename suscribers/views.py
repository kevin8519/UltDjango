from django.contrib.auth.models import User
from django.shortcuts import render

from suscribers.forms import SuscriberForm
from django.http.response import HttpResponseRedirect


# Create your views here.
def suscriber_new(request):
    template='suscribers/subscriber_new.html'
    if request.method=='POST':
        
        form=SuscriberForm(request.POST)
        
        if form.is_valid() :
        
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
        
            user=User(username=username,email=email)
        
            user.set_password(password)
        
            user.save()
            
            return HttpResponseRedirect('/sucess/')
        
    else:
        
        form= SuscriberForm()
        
        
    return render(request,template,{'form':form 
              
              })  
        
    