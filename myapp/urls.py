from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexPage, name = "indexpage"),
    path("register/",views.RegisterPage,name="registerpage"),
    path("registeruser/",views.RegisterUser,name="registeruser"),
    path("loginpage/",views.LoginPage, name = "loginpage"),
    path("loginuser/",views.LoginUser, name="loginuser"),
    path("logoutuser/",views.LogoutUser,name="logoutuser"),
    path("contactpage/",views.ContactPage,name = "contactpage"),
    path("submitquery/",views.SubmitQuery,name="submitquery"),
    path("aboutus/",views.AboutUsPage,name="aboutus")
]