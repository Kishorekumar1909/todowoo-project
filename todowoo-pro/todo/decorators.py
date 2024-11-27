from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def adminonly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
            if group == "site_users":
                messages.warning(request, 'You cant acess this page')
                return redirect('current')
            if request.user.is_superuser:
                messages.info(request,None)
                print("dec")
                return view_func(request, *args, **kwargs)
        print(group)
    return wrapper_function

def useronly(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
            if group == "site_users":
                return view_func(request, *args, **kwargs)
            if request.user.is_superuser:
                messages.warning(request, "You cant acess this page")
                return redirect('admin')
        #print(group)
    return wrapper_function