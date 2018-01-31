from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from .models import Notebook

class CoverView(generic.ListView):
	template_name = 'mysite/cover.html'
	def get_queryset(self):
		return Notebook.objects.all()

class IndexView(generic.ListView):
	template_name = 'mysite/index.html'
	def get_queryset(self):
		return None

class ProfileView(generic.ListView):
	template_name = 'mysite/profile.html'
	def get_queryset(self):
		return None

class NotebookView(generic.ListView):
	template_name = 'mysite/notebook.html'
	model = Notebook
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		notebook_list = context['object_list']
		return context

class ProjectView(generic.ListView):
	template_name = 'mysite/project.html'
	def get_queryset(self):
		return None
	  
		

	