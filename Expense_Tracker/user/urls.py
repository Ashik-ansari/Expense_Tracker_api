from django.urls import path
from user import views
from rest_framework.authtoken.views import obtain_auth_token

app_name= "user"

urlpatterns = [
        path('', views.index,name="index"),
        path('register/',views.register.as_view(), name="register"),
        path('login/',obtain_auth_token,name="login"),
        path('welcome/',views.welcome.as_view(),name="welcome"),
        path('category',views.category.as_view(),name="category"),
        path('expense',views.expense.as_view(),name="expense"),
        path('totalexpense',views.totalexpense,name="totalexpense"),
        path('totalcategoryexpense/<int:id>',views.totalcategoryexpense,name="totalcategoryexpense"),

        

]    
