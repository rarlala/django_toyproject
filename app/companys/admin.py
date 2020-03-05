from django.contrib import admin

from companys.models import Company, Mask_Info


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Mask_Info)
class MaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'price', 'soldout')
