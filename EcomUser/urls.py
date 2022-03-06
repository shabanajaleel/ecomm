from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnhome,name="Home"),
    path('newindex',views.fnindex,name="newindex"),
    path('login_user/',views.fnlogin,name="login_user"),
    path('user_register/',views.fnregister,name="user_register"),
    path('login_otp/',views.fnotplogin,name="login_otp"),
    path('enter_otp/',views.fnenterotp,name="enter_otp"),
    path('logout_user/',views.fnlogout,name="logout_user"),
    # path('register/',views.fnregister,name="register"),
    path('Change_User_Password/',views.fnchangeuserpassword,name="Change_User_Password"),

    path('products/<cat_id>',views.fnproductlist,name="products"),
    path('product_item/<prod_id>',views.fnproductitem,name="product_item"),
    path('new_product',views.fnnewproduct,name="new_product"),

    path('wishlist/',views.fnwishlist,name="wishlist"),
    path('add_to_cart/',views.fncart,name="add_to_cart"),
    path('view_cart/',views.fnviewcart,name="view_cart"),
    path('remove_cart_item/<cart_item_id>',views.fnremovecartitem,name="remove_cart_item"),


    path('contact_us/',views.fnfeedback,name="contact_us")
]