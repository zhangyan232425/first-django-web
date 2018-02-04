from django.contrib import admin

# Register your models here.
from .models import Notebook

class NotebookAdmin(admin.ModelAdmin):
	list_display = ['note_title','note_time']
	list_display_links = ['note_title']
	list_filter = ['note_time']
	search_fields = ['note_title','note_body']

admin.site.register(Notebook,NotebookAdmin)