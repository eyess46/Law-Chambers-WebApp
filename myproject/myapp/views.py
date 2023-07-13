from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Feature, New 
from.models import Contactform


# Create your views here.



def index(request):
    features = Feature.objects.all()
    news = New.objects.all()

    return render(request, 'index.html', {'features': features, 'news': news})


def contact(request):
   
   if request.method == "POST":                    
        name = request.POST.get('name')      
        email = request.POST.get('email')        
        subject = request.POST.get('subject') 
        message = request.POST.get('message')            
                       
        print(name, email, subject, message)            
        Contactform.objects.create(name=name, email=email, subject=subject, message=message,)
        messages.success(request, f'Your Message Has Been Sent Successfully!')       
        return redirect('index')  

   else:
      return render(request, 'contact.html', )



def service(request):
    features = Feature.objects.all()

    return render(request, 'service.html', {'features': features})


def about(request):

    return render(request, 'about.html')
