from dataclasses import fields
from rest_framework import serializers
#from user.models import myuser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from user.models import ExpenseCategory,Expense

User = get_user_model()

class UserRegister(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only = True)

    class Meta:
        model=User
        fields=['first_name','username','email','password','password2']

    def save(self):
        reg=User(
            first_name=self.validated_data['first_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.validationError({'password':'password does not match.'})
        reg.set_password(password)
        reg.save()
        return reg

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','username','email']

class CategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ExpenseCategory
        fields= '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Expense
        fields = ['Category','Description','Date','User','Price','CurrencyType']


class TotalExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['User','Price']

class TotalCategoryExpenseSeriralizer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['Price','Category','User']