from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .models import Contact
from .forms import ContactForm
from .decorators import validate_reCAPTCHA


@validate_reCAPTCHA
def contact(request):
    site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form' : form, 'site_key' : site_key,})



from django.utils.decorators import method_decorator
from django.views.generic import *

class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        context = {
            'form' : self.form_class,
            'site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        return render(request, self.template_name, context)

    @method_decorator(validate_reCAPTCHA)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('contact')

        context = {
            'form' : form,
            'site_key':settings.GOOGLE_RECAPTCHA_SITE_KEY
        }
        return render(request, self.template_name, context)


  

