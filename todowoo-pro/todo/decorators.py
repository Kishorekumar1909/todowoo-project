from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

def adminonly(view_func): # view_func is our calling url function
    def wrapper_function(request, *args, **kwargs): # 'wrapper_sunction' is current url function
        group = None
        if request.user.groups.exists(): # if user in group (we can create group and access the group in django admine site)
            group = request.user.groups.all()[0].name # Getting the groups name where it is presents and just taking first one by slicing method '[0]'
            
            if group == "site_users": # check user in 'site_user' group
                messages.warning(request, 'You cant acess this page') # its True send warning message, used <scrip> alert(messages) </script> in createtodos.html
                return redirect('current')
        if request.user.is_superuser: # user is admin
            messages.info(request,None) # pass message as None 'this line is not mandatory'
            return view_func(request, *args, **kwargs) # its True we allow to call url function what to be call by user.
    return wrapper_function # if not true in any of the condition it return current url with group as "None"

def useronly(view_func): # view_func is our calling url function
    def wrapper_function(request, *args, **kwargs): # 'wrapper_sunction' is current url function
        group = None
        if request.user.groups.exists(): # if user in group (we can create group and access the group in django admine site)
            group = request.user.groups.all()[0].name # Getting the groups name where it is presents and just taking first one by slicing method '[0]'
            
            if group == "site_users":
                return view_func(request, *args, **kwargs) # its True we allow to call url function what to be call by user.
        if request.user.is_superuser: # if user is admin
            messages.warning(request, "You cant acess this page")# its True send warning message, used <scrip> alert(messages) </script> in adminpage.html
            return redirect('admin')
        print(group)
    return wrapper_function # if not true in any of the condition it return current url with group as "None"