from django.db import models
from django.contrib.auth.models import User

# Task management form 
class Todo(models.Model): # 'Todo' is database for user task management.
    title = models.CharField(max_length=100) # Attributes name of databse and its type.
    memo = models.TextField(blank= True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self): # records name of the database
        return self.title