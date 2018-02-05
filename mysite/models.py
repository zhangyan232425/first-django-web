from django.db import models
from django.urls import reverse

class  Notebook(models.Model):
	note_title = models.CharField(max_length=500)
	note_time = models.DateTimeField('data published')
	note_body = models.TextField()

	def __unicode__(self):
		return self.note_title

	def __str__(self):
		return self.note_title

	def get_absolute_url(self):
		return reverse("mysite:notebook_detail",kwargs={"id":self.id})
		
	
			