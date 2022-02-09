from django.urls import path
from . import views

urlpatterns=[ 

    path('contact_us/',views.fnfeedback,name="contact_us")
]