from django.contrib import admin

# Register your models here.
from .models import Customer, Contact

# Register your models here.
admin.site.register(Customer)
admin.site.register(Contact)