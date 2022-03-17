from django.urls import path
from . import views

urlpatterns=[
    path('register_api/',views.fnapi_register,name="register_api")

]