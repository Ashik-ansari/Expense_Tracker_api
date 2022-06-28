from django.contrib import admin
from user.models import ExpenseCategory,Expense

# Register your models here.

admin.site.register(ExpenseCategory)
admin.site.register(Expense)