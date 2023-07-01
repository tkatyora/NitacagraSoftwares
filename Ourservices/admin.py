from django.contrib import admin
from .models import *
from Accounts.models import CustomerWithoutAccount

# # Register your models here.
admin.site.register(CustomerWithoutAccount)
admin.site.register(servicesTable)
admin.site.register(order)
admin.site.register(Functionality)
admin.site.register(Detailed)