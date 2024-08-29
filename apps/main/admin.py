from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'image',
        'text1',
        'title2',
        'text2',
        'title3',
        'text3',
        'title4',
        'text4'
    ]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'message'
    ]



