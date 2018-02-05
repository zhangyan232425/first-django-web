from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Notebook

class CoverView(generic.TemplateView):
	template_name = 'mysite/cover.html'
	

class IndexView(generic.TemplateView):
	template_name = 'mysite/index.html'
	

class ProfileView(generic.TemplateView):
	template_name = 'mysite/profile.html'

class NotebookView(generic.ListView):
	template_name = 'mysite/notebook.html'
	model = Notebook
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		notebook_list = context['object_list']
		return context

def NotebookDetail(request,id = None):
	template_name = 'mysite/notebook_detail.html'
	instance = get_object_or_404(Notebook,id = id)
	context ={
	"title":instance.note_title,
	}
	return render(request,template_name,context)
	
class ProjectView(generic.ListView):
	template_name = 'mysite/project.html'
	def get_queryset(self):
		return None
	  
		

	