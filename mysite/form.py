from django import forms
from pagedown.widgets import PagedownWidget
from mysite.models import Notebook

class BlogForm(forms.ModelForm):
	note_title = forms.CharField()
	note_time = forms.DateField(widget=forms.SelectDateWidget)
	note_body = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Notebook
		fields = ['note_title','note_time','note_body']
			

				
	
