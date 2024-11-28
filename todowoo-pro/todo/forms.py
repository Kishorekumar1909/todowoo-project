from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm): # Form for get the data from users
    class Meta():
        model = Todo # Define the databse to store the data
        fields = ['title', 'memo', 'important'] # field names from above defined model(database)
        # we have to store the datas in 'datecompleted' and 'created' attributes by functions in views.py
