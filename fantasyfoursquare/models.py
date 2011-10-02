from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	points = models.CharField(max_length=200)

	def __unicode__(self):
		return self.username

class Place(models.Model):
	foursquare_id = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	latitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	original_hits = models.IntegerField()
	current_hits = models.IntegerField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
