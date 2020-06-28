from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Laptop, company, orders, service_centers,UserProfile)
class ViewAdmin(admin.ModelAdmin):
    pass
