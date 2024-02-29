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