from django.urls import path
from . import views

urlpatterns=[ 
    path('',views.fnhome,name="Home"),

    path('contact_us/',views.fnfeedback,name="contact_us")
]