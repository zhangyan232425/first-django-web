from django import forms
from pagedown.widgets import PagedownWidget
from mysite.models import Notebook

class BlogForm(forms.Form):
	#note_name = forms.CharField()
	#note_body = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Notebook
		fields = '__all__'
			

				
	
