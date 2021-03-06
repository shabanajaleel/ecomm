from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[ 
    path('home/',views.home,name="home"),

    path('login/',views.fnlogin,name="login"),
    path('logout/',views.fnlogout,name="logout"),
    path('change_password/',views.fnchangepassword,name="change_password"),

    # reset password
    path('password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Admin related urls
    path('add_role/',views.fnaddrole,name="add_role"),
    path('roles/',views.fnrole,name="roles"),
    path('disable_roles/<roledis_id>',views.fndisablerole,name="disable_roles"),
    path('edit_role/<role_id>',views.fneditrole,name="edit_role"),
    path('add_admin/',views.fnaddadmin,name="add_admin"),
    path('view_admin/',views.fnviewadmin,name="view_admin"),
    path('edit_admin/<editadminid>',views.fneditadmin,name="edit_admin"),
    path('disable_admin/<disadminid>',views.fndisableadmin,name="disable_admin"),
    path('add_path/',views.fnaddpath,name="add_path"),
    path('edit_path/<path_id>',views.fneditpath,name="edit_path"),
    path('path/',views.fnpath,name="path"),
    path('disable_path/<pathdis_id>',views.fndisablepath,name="disable_path"),
    path('set_permission/<per_id>',views.fnsetpermission,name="set_permission"),
    path('permission/',views.fnhaspermission,name="permission"),

    path('feedback/',views.fnfeedback,name="feedback"),
    # path('feedback_reply/<feed_id>',views.fnfeedbackreply,name="feedback_reply"),

    path('add_banners/',views.fnaddbanner,name="add_banners"),
    path('addinner_banners/',views.fnaddinnerbanner,name="addinner_banners"),
    path('inner_banners/',views.fninnerbanner,name="inner_banners"),
    path('main_banners/',views.fnmainbanner,name="main_banners"),
    path('maindisplay_order/',views.fnmaindisplay,name="maindisplay_order"),
    path('innerdisplay_order/',views.fninnerdisplay,name="innerdisplay_order"),
    path('edit_innerbanner/<inneredit_id>',views.fneditinner,name="edit_innerbanner"),
    path('disable_innerbanner/<innerban_id>',views.fndisableinnerbanner,name="disable_innerbanner"),
    path('edit_mainbanner/<mainedit_id>',views.fneditmain,name="edit_mainbanner"),
    path('disable_mainbanner/<mainban_id>',views.fndisablemainbanner,name="disable_mainbanner"),

    path('brand/',views.fnbrand,name="brand"),
    path('add_brand/',views.fnaddbrand,name="add_brand"),
    path('edit_brand/<brand_id>',views.fneditbrand,name="edit_brand"),
    path('disable_brand/<branddis_id>',views.fndisablebrand,name="disable_brand"),


    path('catogory/',views.fncatogory,name="catogory"),
    path('add_catogory/',views.fnaddcatogory,name="add_catogory"),
    path('edit_catogory/<cat_id>',views.fneditcatogory,name="edit_catogory"),
    path('disable_catogory/<catdis_id>',views.fndisablecatogory,name="disable_catogory"),
    path('display_order/',views.fndisplay,name="display_order"),
    path('cat_csv/<catcsv_id>',views.fncatcsv,name="cat_csv"),

    path('add_product/',views.fnaddproducts,name="add_product"),
    path('list_product/',views.fnlistproducts,name="list_product"),
    path('edit_product/<editprod_id>',views.fneditproducts,name="edit_product"),
    path('disable_product/<productdis_id>',views.fndisableproduct,name="disable_product"),
    path('view_product/<productview_id>',views.fnviewproducts,name="view_product"),
    path('add_varients/<prodvar_id>',views.fnaddproditems,name="add_varients"),
    path('edit_prodvarients/<edititem_id>',views.fnedititems,name="edit_prodvarients"),
    path('disable_prodvarients/<disitem_id>',views.fndisableitem,name="disable_prodvarients"),
    path('bulk_stock',views.fnbulkstock,name="bulk_stock"),
    path('add_related_products/<prod_id>',views.fnrelatedproducts,name="add_related_products"),


    path('varienttype/',views.fnvarienttype,name="varienttype"),
    path('add_varienttype/',views.fnaddvarienttype,name="add_varienttype"),
    path('edit_varienttype/<var_id>',views.fneditvarienttype,name="edit_varienttype"),
    path('disable_varienttype/<vardis_id>',views.fndisablevarienttype,name="disable_varienttype"),
    path('varient_display_order/',views.fnvarientdisplay,name="varient_display_order"),
    path('varient_select/',views.fnvarientselect,name="varient_select"),

    path('varientvalues/',views.fnvarientvalues,name="varientvalues"),
    path('add_varientvalues/',views.fnaddvarientvalues,name="add_varientvalues"),
    path('edit_varientvalues/<varval_id>',views.fneditvarientvalues,name="edit_varientvalues"),
    path('disable_varientvalues/<disval_id>',views.fndisablevarientvalues,name="disable_varientvalues"),
    path('varientvalues_display_order/',views.fnvarientvaluesdisplay,name="varientvalues_display_order"),


    path('offers/',views.fnoffers,name="offers"),
    path('add_offers/',views.fnaddoffers,name="add_offers"),
    path('edit_offers/<off_id>',views.fneditoffers,name="edit_offers"),
    path('disable_offers/<offdis_id>',views.fndisableoffers,name="disable_offers"),
    path('add_offer_products/<offer_prod>',views.fnofferproducts,name="add_offer_products"),


    path('areas/',views.fnareas,name="areas"),
    path('add_area/',views.fnaddarea,name="add_area"),
    path('add_pincode/<pin_id>',views.fnaddpincode,name="add_pincode"),
    path('disable_area/<disarea_id>',views.fndisablearea,name="disable_area"),
    path('edit_areas/<editarea_id>',views.fneditareas,name="edit_areas"),
    path('disable_pincode/<dispin_id>',views.fndisablepincode,name="disable_pincode"),

    path('customers/',views.fncustomers,name="customers"),
    path('disablecustomer/<customid>',views.fndisablecustomer,name="disablecustomer"),

    path('orders/',views.fnorders,name="orders"),
    path('change_status/',views.fnchangestatus,name="change_status"),
    path('view_orders/<order_id>',views.fnvieworders,name="view_orders"),
    path('delete_item/<prod_id>',views.fndelete_item,name="delete_item"),
    path('delete_order/<prod_id>',views.fndelete_order,name="delete_order"),
    

    path('salesreport',views.fnsalesreport,name="salesreport"),
    path('sales_csv',views.fnsalescsv,name="sales_csv"),
    path('orderreport',views.fnorderreport,name="orderreport"),
    path('order_csv',views.fnordercsv,name="order_csv"),
    path('customerreport',views.fncustomerreport,name="customerreport"),
    path('customer_csv',views.fncustomercsv,name="customer_csv"),

    path('coupon/',views.fncoupon,name="coupon"),
    path('add_coupon/',views.fnaddcoupon,name="add_coupon"),
    path('edit_coupon/<editcoup_id>',views.fneditcoupon,name="edit_coupon"),


    path('deletecustomer/<customid>',views.fndeletecustomer,name="deletecustomer")
   
]