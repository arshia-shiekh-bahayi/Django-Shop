from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from website.forms import ContactForm , NewsletterForm
from django.contrib import messages
# Create your views here.

class IndexView(TemplateView):
    template_name = "website/index.html"

class ContactView(TemplateView):
    template_name = "website/contact.html"

class AboutView(TemplateView):
    template_name = "website/about.html"
    
def contact_view(request):
        if request.method == 'POST':
               form = ContactForm(request.POST)
               if form.is_valid():
                      form.save()
                      messages.add_message(request,messages.SUCCESS,'your ticket had been submited successfully')
               else :
                      messages.add_message(request,messages.ERROR,'your ticket had not been submited successfully')
        form = ContactForm()              
        return render(request,'website/contact.html',{"form":form})
      
def newsletter_view(request):
       if request.method == 'POST':
              form = NewsletterForm(request.POST)
              if form.is_valid():
                     form.save()
                     return HttpResponseRedirect('/')                    
       else :
         return HttpResponseRedirect('/')                     
       form  =ContactForm()
       return render(request,'newsletter.html',{'form':form})
