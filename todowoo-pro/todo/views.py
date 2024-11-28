from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm # Form for geting information about users task 
from .models import Todo # data base for task management
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .decorators import adminonly, useronly # User defined decorators

# Home page for the webpage and look like welcome page
def home(request):
    return render(request, 'todo/home.html')

#signup page for user to sign in
def signupuser(request):
    if request.method == 'GET': # if request in GET method it gives Sign Up form 
        return render(request, 'todo/signupuser.html', {'form' : UserCreationForm()}) # used UserCreationForm() from django forms
    else: # if request in post, post datas fall into authentication
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST["username"],password = request.POST["password1"]) # createing user 
                group = Group.objects.get(name="site_users") 
                user.groups.add(group) # keep the users in seperate group "site_users"
                user.save()
                login(request,user) # login into the page
                return redirect('current')

            except IntegrityError: # if error occurs it throw it in page
                return render(request, 'todo/signupuser.html', {'form' : UserCreationForm(), 'error': "UserName is already taken"})
        else:
            return render(request, 'todo/signupuser.html', {'form' : UserCreationForm(), 'error': "Password is not Mataching"})

# Login functions
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form' : AuthenticationForm()}) # used authentication form by django auth  to get the user credentials.
    else:
        user = authenticate(request, username= request.POST["username"], password= request.POST["password"]) # Authenticating the user credentials by authentication forms and function
        if user is None:
            return render(request, 'todo/loginuser.html', {'form' : AuthenticationForm(), 'error': "Password is wrong"})
        else:
            login(request,user)
            if request.user.is_superuser:
                #login(request,user)
                return redirect('admin')
            return redirect('current')        

#Logout function
@login_required # this decorator only allow when users is logedin.
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


# Create Todo function
@login_required 
@useronly # This is user defined decorator. this decorator only allow the site users. (more information see decorators.py)
def createtodos(request):
    if request=="GET":
        return render(request, 'todo/createtodos.html', {'form' : TodoForm()}) # Todoform helps to get information about user tasks.
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user # assign the task in the name of users by using the ForeignKey in User database.
            newtodo.save()
            return redirect('current')

        except ValueError: # Errors from form 
            return render(request, 'todo/createtodos.html', {'form' : TodoForm(), "error":ValueError})


# current todo function (used to display current task of users)
@login_required
@useronly # Allow only users
def current(request):
    todos = Todo.objects.filter(user= request.user , datecompleted__isnull = True) # important line! to fetch the particular users data(tasks) by using filter() function. User parameter is used fetch particular datas.
    return render(request, 'todo/currentpage.html', {'todos': todos}) # Passing the fetched datas to webpage


# Complete todo function
@login_required
@useronly
def completed(request):# This function helps to show user completed tasks. 
    todos = Todo.objects.filter(user= request.user, datecompleted__isnull = False).order_by('-datecompleted') # Filter() function used to fetch the completed task by the current user 
    # its filter the data by where the 'datecompleted' attributes is not NULL. Because at the creation the record 'datecompleted' is NULL.
    return render(request, 'todo/completed.html', {'todos': todos})


#View todo function
@login_required
def viewtodo(request, todo_pk): # this function helps user to update the Todo tasks like (delete, convert into completed, updations)
    todo = get_object_or_404(Todo, pk= todo_pk, user= request.user) # Important line! that 'todo_pk' varialbe in 'pk' parameter is indicating specific todo task(id) in database
    # [Doing resource access by 'pk= todo_pk, user= request.user']
    if request.method == "GET":
        form = TodoForm(instance= todo) # for updating
        return render(request, 'todo/viewtodo.html', {"todo": todo, 'form' : form})
    else:
        form = TodoForm(request.POST, instance= todo)
        form.save() # after submition (means we get in POST method) our todo form bring updated datas and save it in database.
        return redirect('current')

# this function is play a role for complete button in view page(updation area)
@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk, user= request.user)# Important line! that 'todo_pk' varialbe in 'pk' parameter is indicating specific todo task(id) in database.
    # [Doing resource access by 'pk= todo_pk, user= request.user']
    if request.method == "POST":
        todo.datecompleted = timezone.now() # Assigning the current time and date in the 'datecompleted' its looks like the task is completed.
        todo.save()
        return redirect('current')


# this function is play a role for delete button in view page(updation area)
@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk= todo_pk, user= request.user) # 'todo_pk' is data ID (same as above) [Doing resource access by 'pk= todo_pk, user= request.user']
    if request.method == "POST":
        todo.delete() # it would delete the data from databse
        return redirect('current')
    

@login_required  
@adminonly # This is user defined decorator. this decorator, only allow the admins(superusers). (more information see decorators.py)
def adminpage(request):
    todo = Todo.objects.all # important line! this would bring all the data from database, so we can see all the task created by the users.
    # [Doing resource access by 'objects.all']
    return render(request, 'todo/adminpage.html', {'todos':todo})

