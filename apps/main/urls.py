from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about_us/', AboutUsView.as_view(), name='about'),
    path('contact_us/', ContactUsView.as_view(), name='contact')
]








