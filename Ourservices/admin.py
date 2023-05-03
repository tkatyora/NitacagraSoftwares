from django.contrib import admin
from .models import *
from Accounts.models import customers

# # Register your models here.
admin.site.register(customers)
admin.site.register(servicesTable)
admin.site.register(order)