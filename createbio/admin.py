from django.contrib import admin
from .models import biodata

# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "contact", "email", "address", "city", "state", "pincode", "gender", "education")


admin.site.register(biodata, BiodataAdmin)
