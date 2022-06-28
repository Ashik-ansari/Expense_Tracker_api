from doctest import FAIL_FAST
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User 
import datetime
from djmoney.models.fields import MoneyField
# Create your models here.

class ExpenseCategory(models.Model):
    User         = models.ForeignKey(User, on_delete=models.CASCADE)
    Categoryid   = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=500,null=True)


class Expense(models.Model):
    Expenseid   = models.AutoField(primary_key=True)
    User        = models.ForeignKey(User, on_delete=models.CASCADE)
    Category    = models.ForeignKey(ExpenseCategory,on_delete = models.CASCADE)
    Description = models.CharField(max_length=500,null=True)
    Date        = models.DateField(("Date"), default=datetime.date.today,null=True)
    Price       = models.CharField(max_length=500,null=True)
    CurrencyType= models.CharField(max_length=500, default='INR')
