from django import forms
from pagedown.widgets import PagedownWidget
from mysite.models import Notebook

class BlogForm(forms.ModelForm):
	note_title = forms.CharField(label='Title')
	note_time = forms.DateField(label='Date',widget=forms.SelectDateWidget)
	note_body = forms.CharField(label = 'Content ',widget=PagedownWidget())
	class Meta:
		model = Notebook
		fields = ['note_title','note_time','note_body']
			

				
	
