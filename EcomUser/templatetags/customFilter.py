from django import template

register = template.Library() 

@register.filter
def total_amount(price,discount):
    print(price)
    print(discount)
    
@register.filter
def order_by(queryset,orderby):
    print(queryset)
    some=queryset.order_by(orderby)
    print(some)
    return some

   