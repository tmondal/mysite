from django.contrib import admin
from sms.models import Product


class AdminProduct(admin.ModelAdmin):

	display_fields = ["name", "ptype",'entry_date']

admin.site.register(Product ,AdminProduct)
