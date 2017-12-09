from django.db import models
from django.core.urlresolvers import reverse

class  Notebook(models.Model):
	note_title = models.CharField(max_length=500)
	note_time = models.DateTimeField('data published')
	note_body = models.TextField()
	note_slug = models.SlugField()

	def get_absolute_url(self):
		return reverse('mysite:notebook',kwargs = {self.slug})
	
			