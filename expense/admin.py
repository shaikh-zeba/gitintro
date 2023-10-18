from django.contrib import admin
from .models import ExpenseModel

class ExpenseSchema(admin.ModelAdmin):
    list_display=['id','user','expense_amount','expense_type','expense_date','expense_description',]

admin.site.register(ExpenseModel,ExpenseSchema)

# Register your models here.
