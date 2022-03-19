from django.urls import path
from . import views

urlpatterns=[
    path('register_api/',views.fnapi_register,name="register_api"),
    path('login_api/',views.fnapi_login,name="login_api"),
    path('verifyotp_api/',views.verify_otp,name="verifyotp_api"),
    path('resendotp_api/',views.resend_otp,name="resendotp_api"),

    path('home_api/',views.fnhomeapi,name="home_api"),

    path('add_to_cart_api/',views.fnaddtocart,name="add_to_cart_api"),
    path('view_cart_api/',views.fnviewcart,name="view_cart_api"),
    path('update_cart_api/',views.fnupdatecart,name="update_cart_api"),


    path('add_to_wishlist_api/',views.fnaddtowishlist,name="add_to_wishlist_api")



]