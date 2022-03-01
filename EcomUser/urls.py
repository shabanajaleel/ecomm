from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnhome,name="Home"),
    path('login/',views.fnlogin,name="login"),
    path('logout/',views.fnlogout,name="logout"),
    path('register/',views.fnregister,name="register"),
    path('Change_User_Password/',views.fnchangeuserpassword,name="Change_User_Password"),

    path('wishlist/',views.fnwishlist,name="wishlist"),
    path('addtocart/',views.fncart,name="addtocart"),


    path('contact_us/',views.fnfeedback,name="contact_us")
]