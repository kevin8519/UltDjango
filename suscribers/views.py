from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
import stripe

from forms import SuscriberForm
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
            fee = settings.SUBSCRIPTION_PRICE
            
            try:
                stripe_customer = sub.charge(request, email, fee)
            except stripe.StripeError as e:
                form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])
                return render(request, template,
                              {'form':form,
                               'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY}
                              )
                
            a_u = authenticate(username=username, password=password)
            if a_u is not None:
                if a_u.is_active:
                    login(request, a_u)
                    return HttpResponseRedirect(reverse('account_list'))
                else:
                    return HttpResponseRedirect(
                        reverse('django.contrib.auth.views.login'))
        
            else:
                return HttpResponseRedirect(reverse('sub_new'))
        
    else:
        
        form= SuscriberForm()
        
        
    return render(request,template,{'form':form, 
              
             'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY })  
        
    