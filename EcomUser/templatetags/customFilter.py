from django import template

register = template.Library() 

@register.filter
def total_amount(price,discount):
    print(price)
    print(discount)
    
@register.filter
def remove_duplicate(queryset):
    print(queryset)
   
    print(set([i for i in queryset]))
    return set([i for i in queryset])

   