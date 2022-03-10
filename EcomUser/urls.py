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
    path('addresses/',views.fnaddress,name="addresses"),
    path('add_new_address/',views.fnaddnewaddress,name="add_new_address"),

    path('products/',views.fnproductlist,name="products"),
    path('product_item/<prod_id>',views.fnproductitem,name="product_item"),
    path('new_product',views.fnnewproduct,name="new_product"),
    # path('product_low<cat_id>',views.fnproductlow,name="product_low"),
    
    path('product-offers/',views.fnoffers,name="product-offers"),
    path('new/',views.fnnew,name="new"),



    path('wishlist/',views.fnwishlist,name="wishlist"),
    path('view_wishlist/',views.fnviewwishlist,name="view_wishlist"),
    path('remove_wishlist/',views.fnremovewishlist,name="remove_wishlist"),

    path('add_to_cart/',views.fncart,name="add_to_cart"),
    path('add_to_cart_wish/',views.fnaddtocartwish,name="add_to_cart_wish"),
    path('view_cart/',views.fnviewcart,name="view_cart"),
    path('change_qty',views.fnchangeqty,name="change_qty"),
    path('remove_cart_item/<cart_item_id>',views.fnremovecartitem,name="remove_cart_item"),

    path('checkout/',views.fncheckout,name="checkout"),
    path('select_address/',views.fnselectaddress,name="select_address"),


    path('apply_coupon_code/',views.fncoupon,name="apply_coupon_code"),


    path('contact_us/',views.fnfeedback,name="contact_us")
]