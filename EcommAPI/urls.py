from django.urls import path
from . import views

urlpatterns=[
    # registration and login
    path('register_api/',views.fnapi_register,name="register_api"),
    path('login_api/',views.fnapi_login,name="login_api"),
    path('verifyotp_api/',views.verify_otp,name="verifyotp_api"),
    path('resendotp_api/',views.resend_otp,name="resendotp_api"),

    path('home_api/',views.fnhomeapi,name="home_api"),

    # Products
    path('allproducts_api/',views.fnallproducts,name="allproducts_api"),
    path('product_details_api/',views.fnproductdetails,name="product_details_api"),

    # Cart
    path('add_to_cart_api/',views.fnaddtocart,name="add_to_cart_api"),
    path('view_cart_api/',views.fnviewcart,name="view_cart_api"),
    path('update_cart_api/',views.fnupdatecart,name="update_cart_api"),
    path('remove_cart_api/',views.fnremovecart,name="remove_cart_api"),

    # wishlist
    path('add_to_wishlist_api/',views.fnaddtowishlist,name="add_to_wishlist_api"),
    path('view_wishlist_api/',views.fnviewwishlist,name="view_wishlist_api"),
    path('remove_wishlist_api/',views.fnremovewishlist,name="remove_wishlist_api"),
    path('wishlist_to_cart_api/',views.fnwishtocart,name="wishlist_to_cart_api"),

    



]