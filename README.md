# Ex02 Django ORM Web Application
## Date: 29.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<Er exp2.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.db import models
from django.contrib import admin
class Book(models.Model):
	bid=models.IntegerField(primary_key=True);
	bname=models.CharField(max_length=50);
	price=models.IntegerField();
	author=models.CharField(max_length=50);
	qty=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
	list_display=("bid","bname","price","author","qty");

admin.py
from django.contrib import admin
from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)
```

## OUTPUT
![alt text](<Output exp2.png>)

## RESULT
Thus the program for creating a database using ORM has been executed successfully