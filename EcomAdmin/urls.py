from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.home,name="home"),

    # Admin related urls
    path('add_role/',views.fnaddrole,name="add_role"),

    path('feedback/',views.fnfeedback,name="feedback"),
    # path('feedback_reply/<feed_id>',views.fnfeedbackreply,name="feedback_reply"),

    # path('add_banners/',views.fnaddbanner,name="add_banners"),

    path('brand/',views.fnbrand,name="brand"),
    path('add_brand/',views.fnaddbrand,name="add_brand"),
    path('edit_brand/<brand_id>',views.fneditbrand,name="edit_brand"),
    path('disable_brand/<branddis_id>',views.fndisablebrand,name="disable_brand"),


    path('catogory/',views.fncatogory,name="catogory"),
    path('add_catogory/',views.fnaddcatogory,name="add_catogory"),
    path('edit_catogory/<cat_id>',views.fneditcatogory,name="edit_catogory"),
    path('disable_catogory/<catdis_id>',views.fndisablecatogory,name="disable_catogory"),
    path('display_order/',views.fndisplay,name="display_order"),


    path('varienttype/',views.fnvarienttype,name="varienttype"),
    path('add_varienttype/',views.fnaddvarienttype,name="add_varienttype"),
    path('edit_varienttype/<var_id>',views.fneditvarienttype,name="edit_varienttype"),
    path('disable_varienttype/<vardis_id>',views.fndisablevarienttype,name="disable_varienttype"),
    path('varient_display_order/',views.fnvarientdisplay,name="varient_display_order"),

    path('varientvalues/',views.fnvarientvalues,name="varientvalues"),
    path('add_varientvalues/',views.fnaddvarientvalues,name="add_varientvalues"),
    path('edit_varientvalues/<varval_id>',views.fneditvarientvalues,name="edit_varientvalues"),
    path('disable_varientvalues/<disval_id>',views.fndisablevarientvalues,name="disable_varientvalues"),
    path('varientvalues_display_order/',views.fnvarientvaluesdisplay,name="varientvalues_display_order"),


    path('offers/',views.fnoffers,name="offers"),
    path('add_offers/',views.fnaddoffers,name="add_offers"),
    path('edit_offers/<off_id>',views.fneditoffers,name="edit_offers"),
    path('disable_offers/<offdis_id>',views.fndisableoffers,name="disable_offers"),


    path('areas/',views.fnareas,name="areas"),
    path('add_area/',views.fnaddarea,name="add_area"),
    path('add_pincode/<pin_id>',views.fnaddpincode,name="add_pincode"),
    path('disable_area/<disarea_id>',views.fndisablearea,name="disable_area"),
    path('edit_areas/<editarea_id>',views.fneditareas,name="edit_areas"),
    path('disable_pincode/<dispin_id>',views.fndisablepincode,name="disable_pincode"),




   
]