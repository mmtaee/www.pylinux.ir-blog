from functools import wraps
from django.conf import settings
from django.contrib import messages

import requests

def validate_reCAPTCHA(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        request.recaptcha_is_valid = None
        if request.method == 'POST':
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            # تفاوت این کد با کد v2 در قسمت result  و score می باشد
            if result['success'] and result['score'] >= 0.5:
                request.recaptcha_is_valid = True
            else:
                request.recaptcha_is_valid = False
                messages.error(request, 'Robot detected')
            print(result)
        return view_func(request, *args, **kwargs)
    return wrap