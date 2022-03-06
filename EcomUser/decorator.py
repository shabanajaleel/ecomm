from django.shortcuts import render,redirect

def login_cart(func):
    def wrap(request,*args,**kwargs):
        if request.session.has_key('customer'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/login_user/')
    return wrap
