from django.urls import path

from .views import ContactView, contact

urlpatterns = [
    # path('', contact, name='contact'),
    path('', ContactView.as_view(), name='contact'),
]