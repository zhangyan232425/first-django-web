from django.contrib import admin

# Register your models here.
from .models import Notebook

class NotebookAdmin(admin.ModelAdmin):
	list_display = ['note_title','note_time']

admin.site.register(Notebook,NotebookAdmin)