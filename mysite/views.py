from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Notebook
from mysite.form import BlogForm
from markdown_deux import markdown
from django.utils.safestring import mark_safe

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
	"content":mark_safe(markdown(instance.note_body)),
	}
	return render(request,template_name,context)


	
def NotebookCreate(request):
	#if not request.user.is_staff or not request.user.is_superuser:
	#	raise Http404
		
	form = BlogForm(data=request.POST)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		#messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "mysite/notebook_form.html", context)



	
class ProjectView(generic.ListView):
	template_name = 'mysite/project.html'
	def get_queryset(self):
		return None
	  
		

	