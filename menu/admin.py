from django.contrib import admin
from .models import MenuItem, BusinessHours, ContactInfo

admin.site.register(MenuItem)
admin.site.register(BusinessHours)
admin.site.register(ContactInfo)