from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    tittle = models.CharField(max_length=100)
    memo = models.TextField(blank= True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    completed = models.DateTimeField(null=True, blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle