
import django_filters
from . models import *
from django_filters import DateFilter,CharFilter

class OrderDetailsFilter(django_filters.FilterSet):
    customer=CharFilter(field_name="customer")
    class Meta:
        model=OrderDetails
        fields="__all__"
        exclude=['address','order_date','totalcount','order_total']