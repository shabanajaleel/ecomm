from django import template

register = template.Library() 

@register.filter
def total_amount(price,discount):
    print(price)
    print(discount)
    
@register.filter
def remove_duplicate(queryset):
    print(queryset)
    a=[]
    for i in queryset:
        if i not in a:
            a.append(i)
    print(a)
    return a

@register.filter
def sort_by(queryset,order_by):
    return queryset.order_by(order_by)

   

   