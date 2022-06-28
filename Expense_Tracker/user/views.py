from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView

from user.serializers import UserRegister,CategorySerializer,UserSerializer,ExpenseSerializer,TotalExpenseSerializer,TotalCategoryExpenseSeriralizer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, serializers
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from user.models import ExpenseCategory,Expense
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view


# Create your views here.
User = get_user_model()


def index(request):

    return HttpResponse("EXpense Tracker")

class register(APIView):

    def post(self,request,format=None):
        serializer = UserRegister(data=request.data)
        if serializer.is_valid():
            data={}
            account=serializer.save()
            data['response']='registered'
            data['first_name'] = account.first_name
            data['username']  = account.username
            data['email']     = account.email
            token,create = Token.objects.get_or_create(user=account)
            data['Token']=token.key 
        else:
            data=serializer.errors
        return Response(data)

    def get(self,request,format=None):
        users = User.objects.all()
        user_serializer = UserSerializer(users,many=True)
        return Response(user_serializer.data)

class welcome(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'user' : str(request.user),'userid':str(request.user.id)}
        return Response(content)


class category(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        category = ExpenseCategory.objects.filter(User_id=request.user.id)
        category_serializer = CategorySerializer(category,many=True)
        return Response(category_serializer.data)
    
    def post(self,request,format=None):
        category_serializer=CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            data={}
            category=category_serializer.save()

            data['userid'] = category.User.id
            data['response']='Category Added '
            data['category_name']=category.CategoryName
        else:
            data=category_serializer.errors
        return Response(data)

class expense(APIView):

    def get(self,request,format=None):
        allexpense = Expense.objects.filter(User_id=request.user.id)
        expense_serializer = ExpenseSerializer(allexpense,many=True)
        return Response(expense_serializer.data)
    
    def post(self,request,format=None):
        expense_serializer=ExpenseSerializer(data=request.data)
        if expense_serializer.is_valid():
            data={} 
            expense=expense_serializer.save()
            data['response']    ='Expense Added'
            data['Category']    =expense.Category.CategoryName
            data['Description'] = expense.Description
            data['Price']       = expense.Price
            data['Date']        = expense.Date
            data['CurrencyType']=expense.CurrencyType
        else:
            data=expense_serializer.errors
        return Response(data)

@api_view(['GET'])
def totalexpense(request):
    getexpenses = Expense.objects.filter(User_id=request.user.id)
    data={} 
    totalexpense_serializer=TotalExpenseSerializer(getexpenses,many=True)
    totalexpense=0
    for expen in totalexpense_serializer.data:
        expense= expen['Price']
        totalexpense = totalexpense + int(expense)
   # data['user']=totalexpense_serializer.user
    data['totalexpense'] = totalexpense
    return Response(data)

@api_view(['GET'])
def totalcategoryexpense(request,id):
    getexpense = Expense.objects.filter(User=request.user.id,Category=id)
    data={} 
    totalcategory_serializer=TotalCategoryExpenseSeriralizer(getexpense,many=True)
    totalexpense = 0
    for expen in totalcategory_serializer.data:
        expense      = expen['Price']
        expencategory = expen['Category']
        totalexpense = totalexpense + int(expense)  
    
    data['totalexpensecategory'] = totalexpense
    return Response(data)