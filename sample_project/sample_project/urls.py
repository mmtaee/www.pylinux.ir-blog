from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


# انتقال همه مسیرها برای چند زبانه شدن سایت 
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),

    # اگر این مقدار وارد نشود یا برابر مقدار صحیح قرار گیرد
    # می بایست زبان اصلی و پیشفرض پروژه را نیز در آدرس ها قرار دهیم 
    # /fa/ , /en/ , ....
    prefix_default_language=False,  
)

# برای اضافه شدن آدرس 
# /static/ , /media/
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)