from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnhome,name="Home"),
    path('newindex',views.fnindex,name="newindex"),
    path('login_user/',views.fnlogin,name="login_user"),
    path('login_otp/',views.fnotplogin,name="login_otp"),
    path('enter_otp/',views.fnenterotp,name="enter_otp"),
    path('logout_user/',views.fnlogout,name="logout_user"),
    path('register/',views.fnregister,name="register"),
    path('Change_User_Password/',views.fnchangeuserpassword,name="Change_User_Password"),

    path('wishlist/',views.fnwishlist,name="wishlist"),
    path('addtocart/',views.fncart,name="addtocart"),


    path('contact_us/',views.fnfeedback,name="contact_us")
]