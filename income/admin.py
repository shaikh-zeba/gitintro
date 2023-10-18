from django.contrib import admin

from .models import IncomeModel

class IncomeSchema(admin.ModelAdmin):
    list_display=['id','user','income_amount','income_type','income_date','income_description',]

admin.site.register(IncomeModel,IncomeSchema)


# Register your models here.
