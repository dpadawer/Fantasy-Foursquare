from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	place = models.CharField(max_length=200)

	def __unicode__(self):
		return self.username
