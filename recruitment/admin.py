from django.contrib import admin
from .models import PersonalDetails

# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
    list_display=("id", "applicant_id", "full_name", "parent_name", "dob", "email", "mob_no", "category", "nationality", "gender")

admin.site.register(PersonalDetails, PersonalAdmin)
