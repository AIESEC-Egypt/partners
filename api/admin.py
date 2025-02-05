from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PartnerApplication

@admin.register(PartnerApplication)
class PartnerApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'company_field', 'company_size', 'contact_person_name', 'contact_person_email', 'contact_person_phone')
    search_fields = ('company_name', 'contact_person_name', 'contact_person_email')
    list_filter = ('company_field', 'company_size')
