from django.contrib.auth.models import User
from django.shortcuts import render

from forms import SuscriberForm
from django.http.response import HttpResponseRedirect
from models import Subscriber

# Create your views here.
def suscriber_new(request):
    template='suscribers/subscriber_new.html'
    if request.method=='POST':
        
        form=SuscriberForm(request.POST)
        
        if form.is_valid() :
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
        
            user=User(username=username,email=email)
        
            user.set_password(password)
        
            user.save()
                
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)
            sub.save()
            
            return HttpResponseRedirect('/sucess/')
        
    else:
        
        form= SuscriberForm()
        
        
    return render(request,template,{'form':form 
              
              })  
        
    