from django.urls import path
from . import views

urlpatterns=[
    path('register_api/',views.fnapi_register,name="register_api"),
    path('login_api/',views.fnapi_login,name="login_api"),
    path('verifyotp_api/',views.verify_otp,name="verifyotp_api"),
    path('resendotp_api/',views.resend_otp,name="resendotp_api"),

    path('home_api/',views.fnhomeapi,name="home_api")

]